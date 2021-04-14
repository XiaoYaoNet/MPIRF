# coding=UTF-8

import h5py
import numpy as np
import json
from DataClass.BassClass.ReaderBase import *


class ComplexEnconding(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, complex):
            return "{real}+{image}i".format(real=o.real, image=o.real)


class MDFReaderClass(ReaderBaseClass):

    def __init__(self, SMNameFile, MeasNameFile):
        super().__init__()
        self.__SMNameFile = SMNameFile
        self.__MeasNameFile = MeasNameFile
        self._init_FileHandle()
        self._init_Message()

    def _init_FileHandle(self):

        self.__SMF = h5py.File(self.__SMNameFile, 'r')

        self.__MeasF = h5py.File(self.__MeasNameFile, 'r')

        return True

    def __get_SMData(self):
        S = self.__SMF[SYSMTRMEASDATA]
        return S[:, :, :, :].squeeze()

    def __get_MeasData(self):
        S = self.__MeasF[MEASSIGNALDATA]
        return S[:, :, :, :]

    def __get_BackGround(self):
        S = self.__SMF[ISBACKGROUNDFRAME]
        return S[:].view(bool)

    def __get_SamPointNum(self):
        S = self.__SMF[NUMSAMPLINGPOINTS]
        return int(np.array(S, dtype=np.int32))

    def __get_CaliSize(self):
        S = self.__SMF[CALIBRATIONSIZE]
        return S[:]

    def _init_Message(self):

        self._set_MessageValue(MEASUREMENT, AUXSIGNAL, self.__get_SMData())
        self._set_MessageValue(MEASUREMENT, MEASIGNAL, self.__get_MeasData())
        self._set_MessageValue(MEASUREMENT, TYPE, SYSTEMMATRIX)
        self._set_MessageValue(MEASUREMENT, BGFLAG, self.__get_BackGround())
        self._set_MessageValue(SAMPLE, SAMNUMBER, self.__get_SamPointNum())
        self._set_MessageValue(MEASUREMENT, MEANUMBER, self.__get_CaliSize())

        return True