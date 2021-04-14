# coding=UTF-8

from DataClass.BassClass.ScannerBase import *

class XXXScannerClass(ScannerBaseClass):
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
                 XXXMEMBERTEMPLATE=None):

        super().__init__(VirtualPhantom,
                         SelectGradietX,
                         SelectGradietY,
                         DriveFrequencyX,
                         DriveFrequencyY,
                         DriveAmplitudeX,
                         DriveAmplitudeY,
                         RepetitionTime,
                         SampleFrequency)

        self.XXXMEMBERTEMPLATE=XXXMEMBERTEMPLATE     # Extended member variables

        self.init_Message(3)                 # Set auxiliary signal type

    def get_AuxSignal(self):

        #TODO: add Auxiliary signal calculation process code

        return 0