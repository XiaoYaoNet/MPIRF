#   coding=UTF-8

import numpy as np
import numpy.fft
from Config.ConstantList import *
from PreprocessClass.BaseClass.Preprocess import *
import time

'''
MDFPreprocess.py: override function DataCutting() to add a function removing the low frequency signal from the array of the MeaSignal key.
'''

class MDFPreprocessClass(PreprocessClass):
    def __init__(self,Message):
        self.DataCutting(Message)
        super().__init__(Message)

    #Overriding DataCutting functions
    def DataCutting(self, Message, Threshold=80e3):

        end = np.where(Message[MEASUREMENT][BGFLAG] != 0)
        Message[MEASUREMENT][AUXSIGNAL] = Message[MEASUREMENT][AUXSIGNAL][:, :, 0:end[0][0]]
        Message[MEASUREMENT][MEASIGNAL] = numpy.fft.rfft(Message[MEASUREMENT][MEASIGNAL])
        numfreq = round(int(Message[SAMPLE][SAMNUMBER]) / 2) + 1
        freq = np.arange(0, numfreq) / (numfreq - 1) * Message[SAMPLE][SAMNUMBER]
        idxmin = (freq[:] > Threshold)[0]
        Message[MEASUREMENT][AUXSIGNAL] = Message[MEASUREMENT][AUXSIGNAL][0:2, idxmin:-1, :]

        size = np.shape(Message[MEASUREMENT][MEASIGNAL])
        Message[MEASUREMENT][MEASIGNAL] = np.reshape(Message[MEASUREMENT][MEASIGNAL],
                                                        (size[0] * size[1], size[2], size[3]))

        Message[MEASUREMENT][MEASIGNAL] = Message[MEASUREMENT][MEASIGNAL][:, 0:2, idxmin:-1]

        size = np.shape(Message[MEASUREMENT][AUXSIGNAL])
        Message[MEASUREMENT][AUXSIGNAL] = np.reshape(Message[MEASUREMENT][AUXSIGNAL], (size[0] * size[1], size[2]))

        size = np.shape(Message[MEASUREMENT][MEASIGNAL])
        Message[MEASUREMENT][MEASIGNAL] = np.reshape(Message[MEASUREMENT][MEASIGNAL],
                                                        (size[0], size[1] * size[2]))

        Message[MEASUREMENT][MEASIGNAL] = np.mean(Message[MEASUREMENT][MEASIGNAL], axis=0)

        return True