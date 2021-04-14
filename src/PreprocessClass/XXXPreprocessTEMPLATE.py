#   coding=UTF-8

from PreprocessClass.BaseClass.Preprocess import *

class XXXPreprocessClass(PreprocessClass):
    def __init__(self,Message):
        self.Cutting(Message)
        super().__init__(Message)

    def Cutting(self, Message, Threshold=80e3):
        #TODO: Add specific signal removal code
        return True