# coding=UTF-8

import abc
import numpy as np
from Config.ConstantList import *

'''
Phantom.py: The base class of phantom class.
'''

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

    #Get the volume of magnetic particles.
    def __get_ParticleVolume(self):
        return (self._Diameter ** 3) * PI / 6.0

    # Get the saturation magnetization of the particle.
    def __get_MagMomentSaturation(self):
        return self._MCore * self._Volume

    # Get the property of the particle.
    def __get_ParticleProperty(self):
        return (U0 * self._Mm)/(KB * self._Tt)

    #Return the phantom matrix
    def get_PhantomMatrix(self):
        return self._Picture

    #Abstract function. Return the matrix of the phantom image
    @abc.abstractmethod
    def _get_Picture(self,Concentration,Xn,Yn):
        pass