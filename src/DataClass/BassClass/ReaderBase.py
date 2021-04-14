# coding=UTF-8

from DataClass.BassClass.DataBase import *
from Config.ConstantList import *
import abc


class ReaderBaseClass(DataBaseClass, metaclass=abc.ABCMeta):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        super().__init__()

    @abc.abstractmethod
    def _init_FileHandle(self): pass

    def _init_Message(self): pass