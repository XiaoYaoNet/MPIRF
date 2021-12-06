# coding=UTF-8

from DataClass.BassClass.DataBase import *
from Config.ConstantList import *
import abc

'''
ReaderBase.py: The base class of the Reader component.
'''

class ReaderBaseClass(DataBaseClass, metaclass=abc.ABCMeta):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        super().__init__()

    #Abstract function. Initialize the File handle.
    @abc.abstractmethod
    def _init_FileHandle(self): pass

    # #Initialize the Message.
    def _init_Message(self): pass