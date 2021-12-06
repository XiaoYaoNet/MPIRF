# coding=UTF-8

import abc
from Config.ConstantList import *

'''
DataBase.py: The base class of the data access module.
'''

class DataBaseClass(metaclass=abc.ABCMeta):
    def __init__(self):
        #Define the Message dictionary
        self.Message = {
            MAGNETICPARTICL:{
                DIAMETER : None,
                SATURATIONMAG : None,
                TEMPERATURE : None,
            },
            SELECTIONFIELD:{
                XGRADIENT:None,
                YGRADIENT:None,
                ZGRADIENT:None,
            },
            DRIVEFIELD:{
                XDIRECTIOND:None,
                YDIRECTIOND:None,
                ZDIRECTIOND:None,
                REPEATTIME:None,
                WAVEFORMD:None,
            },
            FOCUSFIELD:{
                XDIRECTIONF:None,
                YDIRECTIONF:None,
                ZDIRECTIONF:None,
                WAVEFORMF:None,
            },
            SAMPLE:{
                TOPOLOGY:None,
                FREQUENCY:None,
                SAMNUMBER:None,
                BEGINTIME:None,
                SENSITIVITY:None,
            },
            MEASUREMENT:{
                TYPE:None,
                BGFLAG:None,
                MEASIGNAL:None,
                AUXSIGNAL:None,
                MEANUMBER:None,
            }
        }

    #Abstract function. Initialize the Message dictionary.
    @abc.abstractmethod
    def _init_Message(self): pass

    def _set_MessageValue(self,ObjectStr,KeyStr,ValueStr):
        self.Message[ObjectStr][KeyStr]=ValueStr


