# coding=UTF-8

import matplotlib.pyplot as plt
import numpy as np
from DataClass.BassClass.ScannerBase import *

class XScannerClass(ScannerBaseClass):
    def __init__(self,
                 VirtualPhantom,
                 SelectGradietX=2.0,
                 SelectGradietY=2.0,
                 DriveFrequencyX=2500000.0 / 102.0,
                 DriveFrequencyY=2500000.0 / 96.0,
                 DriveAmplitudeX=12e-3,
                 DriveAmplitudeY=12e-3,
                 RepetitionTime=6.528e-4,
                 SampleFrequency=2.5e6):

        super().__init__(VirtualPhantom,
                         SelectGradietX,
                         SelectGradietY,
                         DriveFrequencyX,
                         DriveFrequencyY,
                         DriveAmplitudeX,
                         DriveAmplitudeY,
                         RepetitionTime,
                         SampleFrequency)
        self._init_Message(2)
        self.Message[EXTENDED]= {STEP:self._Step,RFFP:self._Rffp2,FFP:self._Rffp0}

    # Calculate the field-free area velocity vector.
    def _get_AuxSignal(self):
        return np.divide(self._DeriDH, np.tile(self._Gg, (1, np.shape(self._DeriDH)[1])))