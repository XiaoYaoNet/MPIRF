# coding=UTF-8

from DataClass.BassClass.ReaderBase import *
import json
import numpy as np

class JsonDefaultEnconding(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, complex):
            return "{real}+{image}i".format(real=o.real, image=o.real)
        if isinstance(o, np.ndarray):
            return o.tolist()

class JReaderClass(ReaderBaseClass):
    def __init__(self, JNameFile):
        super().__init__()
        self.__JNameFile = JNameFile
        self._init_FileHandle()
        self._init_Message()

    def _init_FileHandle(self):
        with open(self.__JNameFile, 'r', encoding='utf8') as fp:
            self.Message = json.load(fp)

        return True

    def _init_Message(self):

        if self.Message[MEASUREMENT][TYPE]==SYSTEMMATRIX:
            self.Message[MEASUREMENT][AUXSIGNAL]=np.array(self.Message[MEASUREMENT][AUXSIGNAL],dtype=complex)
            self.Message[MEASUREMENT][MEASIGNAL]=np.array(self.Message[MEASUREMENT][MEASIGNAL],dtype=complex)
        else:
            self.Message[MEASUREMENT][AUXSIGNAL] = np.array(self.Message[MEASUREMENT][AUXSIGNAL], dtype=float)
            self.Message[MEASUREMENT][MEASIGNAL] = np.array(self.Message[MEASUREMENT][MEASIGNAL], dtype=float)

        self.Message[MEASUREMENT][BGFLAG]=np.array(self.Message[MEASUREMENT][BGFLAG],dtype=bool)
        self.Message[MEASUREMENT][MEANUMBER]=np.array(self.Message[MEASUREMENT][MEANUMBER],dtype=int)

        return True

if __name__ == "__main__":
    pass