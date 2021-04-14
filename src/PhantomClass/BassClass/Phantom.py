# coding=UTF-8

import abc
import numpy as np
from Config.ConstantList import *

class PhantomClass(metaclass=abc.ABCMeta):
    def __init__(self,Temperature,Diameter,MagSaturation, Concentration ):

        self._Tt = Temperature + TDT
        self._Diameter = Diameter
        self._Volume = self.__get_ParticleVolume()
        self._MCore = MagSaturation
        self._Mm = self.__get_MagMomentSaturation()
        self._Bcoeff = self.__get_ParticleProperty()
        self._Xn=0
        self._Yn=0
        self._Picture =None
        self._Concentration = Concentration

    def __get_ParticleVolume(self):
        return (self._Diameter ** 3) * PI / 6.0

    def __get_MagMomentSaturation(self):
        return self._MCore * self._Volume

    def __get_ParticleProperty(self):
        return (U0 * self._Mm)/(KB * self._Tt)

    def get_PhantomMatrix(self):
        return self._Picture

    @abc.abstractmethod
    def _get_Picture(self,Concentration,Xn,Yn):
        pass