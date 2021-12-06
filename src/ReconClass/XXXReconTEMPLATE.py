# coding=UTF-8
from ReconClass.BaseClass.ReconBase import *
from Config.ConstantList import *

'''
This is a template file.
'''

class XXXReconClass(ReconBaseClass):
    def __init__(self, Message,XXXMEMBERTEMPLATE):
        super().__init__()
        self.XXXMEMBERTEMPLATE = XXXMEMBERTEMPLATE  # Extended member variables
        self._ReconImage_Method(Message)
    def _ReconImage_Method(self,Message):
        self.ImagSignal.append(self.__XXXMETHODTEMPLATE(Message[MEASUREMENT][AUXSIGNAL],
                                                        Message[MEASUREMENT][MEASIGNAL]))
        self.ImagSignal.append(self._Image())
    def _Image(self):
        #self.ImagSignal[0]: is the image data
        #TODO: Add your image data resizing code
        return 0
    def __XXXMETHODTEMPLATE(self,Auxsignal , Measignal):
        # Auxsignal: Measured data of target phantom
        # Measignal: Auxiliary measured data for reconstruction
        #TODO: Add your image reconstruction code here
        return 0



