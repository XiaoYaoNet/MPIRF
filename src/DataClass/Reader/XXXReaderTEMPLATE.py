# coding=UTF-8

from DataClass.BassClass.ReaderBase import *

'''
This is a template file.
'''

class XXXReaderClass(ReaderBaseClass):
    def __init__(self, JNameFile):
        super().__init__()
        self.JNameFile = JNameFile           #MPI Offline file direction and name
        self.init_FileHandle()
        self.init_Message()

    def init_FileHandle(self):
        #TODO: add open JNameFile code
        pass

    def get_SMData(self):
        #TODO: ADD read measurement data from JNameFile code
        return 0

    def init_Message(self):
        self.set_MessageValue(MEASUREMENT, MEASIGNAL, self.get_SMData())
        #TODO: ADD Fill in the Message code
        pass
