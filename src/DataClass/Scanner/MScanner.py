# coding=UTF-8
import numpy as np

from DataClass.BassClass.ScannerBase import *


class MScannerClass(ScannerBaseClass):

    def __init__(self,
                 VirtualPhantom,
                 SelectGradietX=2.0,
                 SelectGradietY=2.0,
                 DriveFrequencyX=2500000.0 / 102.0,
                 DriveFrequencyY=2500000.0 / 96.0,
                 DriveAmplitudeX=12e-3,
                 DriveAmplitudeY=12e-3,
                 RepetitionTime=6.528e-4,
                 SampleFrequency=2.5e6,
                 DeltaConcentration=50e-3):

        super().__init__(VirtualPhantom,
                         SelectGradietX,
                         SelectGradietY,
                         DriveFrequencyX,
                         DriveFrequencyY,
                         DriveAmplitudeX,
                         DriveAmplitudeY,
                         RepetitionTime,
                         SampleFrequency)

        self.__DeltaConcentration=DeltaConcentration
        self._init_Message(1)
        self.__reset_Voltage()

    def __reset_Voltage(self):
        self.Message[MEASUREMENT][MEASIGNAL] = np.transpose(self.Message[MEASUREMENT][MEASIGNAL])
        temp = np.fft.fft(np.transpose(self.Message[MEASUREMENT][MEASIGNAL]) * 1000)
        temp = np.transpose(temp)
        self.Message[MEASUREMENT][MEASIGNAL] = np.add(temp[:, 0], temp[:, 1])
        return True

    def _get_AuxSignal(self):

        C = np.ones((self._Xn, self._Yn,2))
        C = C * self.__DeltaConcentration
        AuxSignal=np.zeros((self._Fn,self._Xn,self._Yn,2))
        DLF = np.zeros((self._Xn, self._Yn, 2))
        for i in range(self._Fn):
            Coeff = self._CoilSensitivity * self._Phantom._Mm * self._Phantom._Bcoeff * self._DeriDH[:, i]
            DLFTemp = (1 / ((self._Phantom._Bcoeff * self._HFieldStrength[:, :, i]) ** 2)) - (
                        1 / ((np.sinh(self._Phantom._Bcoeff * self._HFieldStrength[:, :, i])) ** 2))
            DLF[:, :, 0] = DLFTemp
            DLF[:, :, 1] = DLFTemp
            s = C * Coeff
            AuxSignal[i, :, :, :] = s * DLF

        AuxSignal = np.reshape(AuxSignal, (self._Fn,self._Xn*self._Yn,2))
        AuxSignal = AuxSignal / self.__DeltaConcentration
        tempx = AuxSignal[:, :, 0]
        tempy = AuxSignal[:, :, 1]

        tempx = np.fft.fft(np.transpose(tempx) * 1000)
        tempy = np.fft.fft(np.transpose(tempy) * 1000)
        AuxSignal = np.transpose(np.add(tempx, tempy))
        return AuxSignal