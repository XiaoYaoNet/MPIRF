# coding=UTF-8

from DataClass.BassClass.DataBase import *
import abc
import numpy as np
from Config.CommFunc import *
from Config.ConstantList import *

'''
ScannerBase.py: The base class of the Simulation component.
'''

class ScannerBaseClass(DataBaseClass, metaclass=abc.ABCMeta):
    __metaclass__ = abc.ABCMeta

    def __init__(self,
                 VirtualPhantom,
                 SelectGradietX,
                 SelectGradietY,
                 DriveFrequencyX,
                 DriveFrequencyY,
                 DriveAmplitudeX,
                 DriveAmplitudeY,
                 RepetitionTime,
                 SampleFrequency
                 ):
        super().__init__()

        self._Phantom=VirtualPhantom

        self._CoilSensitivity = 1.0

        self._Gx = SelectGradietX / U0
        self._Gy = SelectGradietY / U0
        self._Gg = np.array([[self._Gx], [self._Gy]])

        self._Fx = DriveFrequencyX
        self._Fy = DriveFrequencyY
        self._Tr = RepetitionTime

        self._Ay = DriveAmplitudeX / U0
        self._Ax = DriveAmplitudeY / U0

        self._Fs = SampleFrequency

        self._Fn = round(self._Tr * self._Fs)

        self._Xmax = self._Ax / self._Gx
        self._Ymax = self._Ay / self._Gy

        self._Step = 1e-4

        self._XSquence = np.arange(-self._Xmax, self._Xmax + self._Step, self._Step)
        self._YSquence = np.arange(-self._Ymax, self._Ymax + self._Step, self._Step)
        self._Xn = len(self._YSquence)
        self._Yn = len(self._XSquence)

        self._TSquence = np.arange(0, self._Tr + self._Tr / self._Fn, self._Tr / self._Fn)

        self._DHx, self._DeriDHx = self.__DriveStrength(self._Ax, self._Fx, self._TSquence)
        self._DHy, self._DeriDHy = self.__DriveStrength(self._Ay, self._Fy, self._TSquence)

        self._DH = np.array([self._DHx, self._DHy])
        self._DeriDH = np.array([self._DeriDHx, self._DeriDHy])

        self._Rffp = np.divide(self._DH, np.tile(self._Gg, (1, np.shape(self._DH)[1])))

        self._Rffp0=self._Rffp
        self._Xffp = self._Rffp[0]
        self._Yffp = self._Rffp[1]

        self._Rffp = self.__MAPPING()

    '''
        Since the image data is stored in an array in the computer, 
        whose coordinate is different from the coordinate system used to scans the phantom, 
        the MAPPING function converts coordinates to body membrane space coordinates.
    '''
    def __MAPPING(self):
        self._Rffp[0] = self._Rffp[0] + self._Xmax
        self._Rffp[1] = self._Rffp[1] - self._Ymax
        self._Rffp[1] = self._Rffp[1] * -1
        self._Rffp2=self._Rffp
        self._Rffp = self._Rffp * (1/self._Step)
        self._Rffp1=self._Rffp
        return np.around(self._Rffp) + 1

    #Calculate the driving field strength.
    def __DriveStrength(self,DriveAmplitude,DriveFrequency,TSquence):
        DHx = DriveAmplitude * np.cos(2.0 * PI * DriveFrequency * TSquence + PI / 2.0) * (-1.0)
        DeriDHx = DriveAmplitude * np.sin(2.0 * PI * DriveFrequency * TSquence + PI / 2.0) * 2.0 * PI * DriveFrequency
        return DHx,DeriDHx

    #Initialize the phantom.
    def __init_Phantom(self):
        self._Phantom._Picture = self._Phantom._get_Picture(self._Phantom._Concentration, self._Xn, self._Yn)
        GSc = np.zeros((self._Xn, self._Yn, 2))
        for i in range(self._Xn):
            y = (i) * (1e-4) * (-1) + self._Ymax
            for j in range(self._Yn):
                x = (j) * (1e-4) - self._Xmax
                temp=self._Gg*[[x], [y]]
                GSc[i, j, 0] = temp[0]
                GSc[i, j, 1] = temp[1]
        self._Fn=self._Fn+1
        return GSc

    #Calculate the induced voltage of magnetic particles with GPU.
    def _get_Voltage_GPU(self):

        GSc = self.__init_Phantom()

        Voltage = np.zeros((2, self._Fn))

        self._HFieldStrength = np.zeros((self._Xn, self._Yn, self._Fn))

        for i in range(self._Fn):
            Coeff = self._CoilSensitivity * self._Phantom._Mm * self._Phantom._Bcoeff * self._DeriDH[:, i]
            DHt = np.tile(self._DH[:, i], (self._Xn, self._Yn, 1))
            Gs = np.subtract(DHt, GSc)
            self._HFieldStrength[:, :, i] = np.sqrt(Gs[:, :, 1] ** 2 + Gs[:, :, 0] ** 2)
            DLFTemp = (1 / ((self._Phantom._Bcoeff * self._HFieldStrength[:, :, i]) ** 2)) - (
                        1 / ((np.sinh(self._Phantom._Bcoeff * self._HFieldStrength[:, :, i])) ** 2))
            DLF = np.zeros((self._Xn, self._Yn, 2))
            DLF[:, :, 0] = DLFTemp
            DLF[:, :, 1] = DLFTemp

            Phanpic = np.tile(np.transpose(self._Phantom._Picture), (2, 1, 1))
            Phanpic = np.transpose(Phanpic)
            Coeff = np.tile(Coeff, (self._Xn, self._Yn, 1))
            Voltage[0, i] = np.sum(MNPMultiply(Phanpic[:,:,0] , Coeff[:,:,0] , DLF[:,:,0]))
            Voltage[1, i] = np.sum(MNPMultiply(Phanpic[:,:,1] , Coeff[:,:,1] , DLF[:,:,1]))
            temp=0

        return Voltage

    # Calculate the induced voltage of magnetic particles with CPU.
    def _get_Voltage_CPU(self):

        GSc=self.__init_Phantom()

        Voltage = np.zeros((2, self._Fn))

        self._HFieldStrength=np.zeros((self._Xn,self._Yn,self._Fn))

        for i in range(self._Fn):
            Coeff = self._CoilSensitivity * self._Phantom._Mm * self._Phantom._Bcoeff * self._DeriDH[:, i]
            DHt = np.tile(self._DH[:, i], (self._Xn, self._Yn, 1))
            Gs = np.subtract(DHt, GSc)
            self._HFieldStrength[:, :, i ] = np.sqrt(Gs[:, :, 1] ** 2 + Gs[:, :, 0] ** 2)
            DLFTemp = (1 / ((self._Phantom._Bcoeff * self._HFieldStrength[:, :, i ]) ** 2)) - (1 / ((np.sinh(self._Phantom._Bcoeff * self._HFieldStrength[:, :, i ])) ** 2))
            DLF=np.zeros((self._Xn, self._Yn, 2))
            DLF[:, :, 0]=DLFTemp
            DLF[:, :, 1] = DLFTemp

            Phanpic = np.tile(np.transpose(self._Phantom._Picture), (2, 1, 1))
            Phanpic = np.transpose(Phanpic)
            Coeff = np.tile(Coeff, (self._Xn, self._Yn, 1))
            s = Phanpic * Coeff
            Sig = s * DLF
            Voltage[0, i] = np.sum(Sig[:, :, 0])
            Voltage[1, i] = np.sum(Sig[:, :, 1])

        return Voltage

    #Abstract function. Calculate the calculate auxiliary signal, such as system matrix.
    @abc.abstractmethod
    def _get_AuxSignal(self):
        pass

    def _get_Signal(self):

        Voltage = self._get_Voltage_CPU()

        AuxSignal = self._get_AuxSignal()

        return Voltage, AuxSignal

    # #Initialize the Message.
    def _init_Message(self,AuxType):

        Voltage, AuxSignal=self._get_Signal()

        self._set_MessageValue(MAGNETICPARTICL, TEMPERATURE, self._Phantom._Tt)
        self._set_MessageValue(MAGNETICPARTICL, DIAMETER, self._Phantom._Diameter)
        self._set_MessageValue(MAGNETICPARTICL, SATURATIONMAG, self._Phantom._Mm)

        self._set_MessageValue(SELECTIONFIELD, XGRADIENT, self._Gx)
        self._set_MessageValue(SELECTIONFIELD, YGRADIENT, self._Gy)

        self._set_MessageValue(DRIVEFIELD, XDIRECTIOND, np.array([self._Ax, self._Fx, 0]))
        self._set_MessageValue(DRIVEFIELD, YDIRECTIOND, np.array([self._Ay, self._Fy, 0]))
        self._set_MessageValue(DRIVEFIELD, REPEATTIME, self._Tr)
        self._set_MessageValue(DRIVEFIELD, WAVEFORMD, SINE)

        self._set_MessageValue(SAMPLE, TOPOLOGY, FFL)
        self._set_MessageValue(SAMPLE, FREQUENCY, self._Fs)
        self._set_MessageValue(SAMPLE, SAMNUMBER, self._Fn)
        self._set_MessageValue(SAMPLE, BEGINTIME, None)
        self._set_MessageValue(SAMPLE, SENSITIVITY, self._CoilSensitivity)

        self._set_MessageValue(MEASUREMENT, TYPE, AuxType)
        self._set_MessageValue(MEASUREMENT, BGFLAG, np.ones(np.shape(Voltage),dtype='bool'))
        self._set_MessageValue(MEASUREMENT, MEASIGNAL, Voltage)
        self._set_MessageValue(MEASUREMENT, AUXSIGNAL, AuxSignal)
        self._set_MessageValue(MEASUREMENT, MEANUMBER, np.array([self._Xn, self._Yn], dtype='int64'))

        return True




