#   coding=UTF-8

import numpy as np
import numpy.fft
from Config.ConstantList import *
import time

'''
Preprocess.py: The base class of the Pre-processing module.
'''

class PreprocessClass(object):

    def __init__(self, Message):
        code,object,key=self.DataValidation(Message)
        if code==False:
            print("Preprocess class: Message["+object+ "]["+key+"] Datavalidation() fail!")

    #Compare data types.
    def _get_Type(self, variate,type):
        if isinstance(variate, type):
            return True
        elif type==float and isinstance(variate, int):
            return True
        else:
            return False

    #Compare the types of array elements.
    def _get_TypeArray(self, variate, type1):
        if str(variate.dtype) in type1:
            return True
        else:
            return False

    # Compare the types of array elements.
    def _get_TypeArray2(self, variate, type1, type2):
        if str(variate.dtype) in type1 or str(variate.dtype) in type2:
            return True
        else:
            return False

    #To verify whether all key-values whose value is non-None in the Message correspond to defined data types.
    def DataValidation(self, Message):

        # MAGNETICPARTICL Object
        if not Message[MAGNETICPARTICL][DIAMETER] is None:
            flag = self._get_Type(Message[MAGNETICPARTICL][DIAMETER], float)
            if flag == False:
                return False, MAGNETICPARTICL, DIAMETER

        if not Message[MAGNETICPARTICL][SATURATIONMAG] is None:
            flag = self._get_Type(Message[MAGNETICPARTICL][SATURATIONMAG], float)
            if flag == False:
                return False, MAGNETICPARTICL, SATURATIONMAG

        if not Message[MAGNETICPARTICL][TEMPERATURE] is None:
            flag = self._get_Type(Message[MAGNETICPARTICL][TEMPERATURE], float)
            if flag == False:
                return False, MAGNETICPARTICL, TEMPERATURE

        # SELECTIONFIELD Object
        if not Message[SELECTIONFIELD][XGRADIENT] is None:
            flag = self._get_Type(Message[SELECTIONFIELD][XGRADIENT], float)
            if flag == False:
                return False, SELECTIONFIELD, XGRADIENT

        if not Message[SELECTIONFIELD][YGRADIENT] is None:
            flag = self._get_Type(Message[SELECTIONFIELD][YGRADIENT], float)
            if flag == False:
                return False, SELECTIONFIELD, YGRADIENT

        if not Message[SELECTIONFIELD][ZGRADIENT] is None:
            flag = self._get_Type(Message[SELECTIONFIELD][ZGRADIENT], float)
            if flag == False:
                return False, SELECTIONFIELD, ZGRADIENT

        # DRIVEFIELD Object
        if not Message[DRIVEFIELD][XDIRECTIOND] is None:
            flag = self._get_TypeArray(Message[DRIVEFIELD][XDIRECTIOND], ["float","float32","float64","float128"])
            if flag == False:
                return False, DRIVEFIELD, XDIRECTIOND

        if not Message[DRIVEFIELD][YDIRECTIOND] is None:
            flag = self._get_TypeArray(Message[DRIVEFIELD][YDIRECTIOND], ["float","float32","float64","float128"])
            if flag == False:
                return False, DRIVEFIELD, YDIRECTIOND

        if not Message[DRIVEFIELD][ZDIRECTIOND] is None:
            flag = self._get_TypeArray(Message[DRIVEFIELD][ZDIRECTIOND], ["float","float32","float64","float128"])
            if flag == False:
                return False, DRIVEFIELD, ZDIRECTIOND

        if not Message[DRIVEFIELD][REPEATTIME] is None:
            flag = self._get_Type(Message[DRIVEFIELD][REPEATTIME], float)
            if flag == False:
                return False, DRIVEFIELD, REPEATTIME

        if not Message[DRIVEFIELD][WAVEFORMD] is None:
            flag = self._get_Type(Message[DRIVEFIELD][WAVEFORMD], int)
            if flag == False:
                return False, DRIVEFIELD, WAVEFORMD

        # FOCUSFIELD Object
        if not Message[FOCUSFIELD][XDIRECTIONF] is None:
            flag = self._get_TypeArray(Message[FOCUSFIELD][XDIRECTIONF], ["float","float32","float64","float128"])
            if flag == False:
                return False, FOCUSFIELD, XDIRECTIONF

        if not Message[FOCUSFIELD][YDIRECTIONF] is None:
            flag = self._get_TypeArray(Message[FOCUSFIELD][YDIRECTIONF], ["float","float32","float64","float128"])
            if flag == False:
                return False, FOCUSFIELD, YDIRECTIONF

        if not Message[FOCUSFIELD][ZDIRECTIONF] is None:
            flag = self._get_TypeArray(Message[FOCUSFIELD][ZDIRECTIONF], ["float","float32","float64","float128"])
            if flag == False:
                return False, FOCUSFIELD, ZDIRECTIONF

        if not Message[FOCUSFIELD][WAVEFORMF] is None:
            flag = self._get_Type(Message[FOCUSFIELD][WAVEFORMF], int)
            if flag == False:
                return False, FOCUSFIELD, WAVEFORMF

        # SAMPLE Object
        if not Message[SAMPLE][TOPOLOGY] is None:
            flag = self._get_Type(Message[SAMPLE][TOPOLOGY], int)
            if flag == False:
                return False, SAMPLE, TOPOLOGY

        if not Message[SAMPLE][FREQUENCY] is None:
            flag = self._get_Type(Message[SAMPLE][FREQUENCY], float)
            if flag == False:
                return False, SAMPLE, FREQUENCY

        if not Message[SAMPLE][SAMNUMBER] is None:
            flag = self._get_Type(Message[SAMPLE][SAMNUMBER], int)
            if flag == False:
                return False, SAMPLE, SAMNUMBER

        if not Message[SAMPLE][BEGINTIME] is None:
            flag = self._get_Type(Message[SAMPLE][BEGINTIME], float)
            if flag == False:
                return False, SAMPLE, BEGINTIME

        if not Message[SAMPLE][SENSITIVITY] is None:
            flag = self._get_Type(Message[SAMPLE][SENSITIVITY], float)
            if flag == False:
                return False, SAMPLE, SENSITIVITY

        # MEASUREMENT Object
        flag = self._get_Type(Message[MEASUREMENT][TYPE], int)
        if flag == False:
            return False, MEASUREMENT, TYPE

        flag = self._get_TypeArray2(Message[MEASUREMENT][BGFLAG], ["bool"],["int","int16","int32","int64"])
        if flag == False:
            return False, MEASUREMENT, BGFLAG

        flag = self._get_TypeArray2(Message[MEASUREMENT][MEASIGNAL], ["complex64","complex128"], ["float","float32","float64","float128"])
        if flag == False:
            return False, MEASUREMENT, MEASIGNAL

        flag = self._get_TypeArray2(Message[MEASUREMENT][AUXSIGNAL], ["complex64","complex128"], ["float","float32","float64","float128"])
        if flag == False:
            return False, MEASUREMENT, AUXSIGNAL

        flag = self._get_TypeArray(Message[MEASUREMENT][MEANUMBER], ["int","int16","int32","int64"])
        if flag == False:
            return False, MEASUREMENT, MEANUMBER

        return True,"",""

    #To performs special deal with the key-values in the Message structure.
    def DataStandardization(self, Message):
        mm=0.0
        b0=0.0
        Message[MEASUREMENT][MEASIGNAL]=Message[MEASUREMENT][MEASIGNAL]/KB

        if not Message[SAMPLE][SENSITIVITY] is None:
            Message[MEASUREMENT][MEASIGNAL]=Message[MEASUREMENT][MEASIGNAL]/Message[SAMPLE][SENSITIVITY]

        if (not Message[MAGNETICPARTICL][DIAMETER] is None) and (not Message[MAGNETICPARTICL][SATURATIONMAG] is None):
            mm=Message[MAGNETICPARTICL][SATURATIONMAG] * ((Message[MAGNETICPARTICL][DIAMETER] ** 3) * PI / 6.0)
            Message[MEASUREMENT][MEASIGNAL] = Message[MEASUREMENT][MEASIGNAL] / mm

            if not Message[MAGNETICPARTICL][TEMPERATURE] is None:
                b0=U0*mm/(Message[MAGNETICPARTICL][TEMPERATURE]*KB)
                Message[MEASUREMENT][MEASIGNAL] = Message[MEASUREMENT][MEASIGNAL] / b0

        return True

    #To remove certain signal data from the array of MeaSiganl key and AuxSiganl key of Measurement object in Message
    def DataCutting(self,Message):
        Message[MEASUREMENT][AUXSIGNAL] = Message[MEASUREMENT][AUXSIGNAL][:, :, Message[SAMPLE][BGFLAG] == False]

        return True