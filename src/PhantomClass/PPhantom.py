# coding=UTF-8
import numpy as np
from Config.ConstantList import *
from PhantomClass.BassClass.Phantom import *

'''
PPhantom.py: The phantom class of P shape.
'''

class PPhantomClass(PhantomClass):
    def __init__(self,Temperature=20.0,Diameter=30e-9,MagSaturation=8e5, Concentration=5e7 ):

        super().__init__(Temperature,
                         Diameter,
                         MagSaturation,
                         Concentration)

    # Return the matrix of the 'P' phantom image.
    def _get_Picture(self,Concentration,Xn,Yn):
        self._Xn = Xn
        self._Yn = Yn
        C = np.zeros((self._Xn, self._Yn))
        C[int(Xn * (14 / 121)):int(Xn * (105 / 121)), int(Yn * (29 / 121)):int(Yn * (90 / 121))] = np.ones(
            (int(Xn * (105 / 121)) - int(Xn * (14 / 121)), int(Yn * (90 / 121)) - int(Yn * (29 / 121))))
        C[int(Xn * (29 / 121)):int(Xn * (60 / 121)), int(Yn * (44 / 121)):int(Yn * (75 / 121))] = np.zeros(
            (int(Xn * (60 / 121)) - int(Xn * (29 / 121)), int(Yn * (75 / 121)) - int(Yn * (44 / 121))))
        C[int(Xn * (74 / 121)):int(Xn * (105 / 121)), int(Yn * (44 / 121)):int(Yn * (90 / 121))] = np.zeros(
            (int(Xn * (105 / 121)) - int(Xn * (74 / 121)), int(Yn * (90 / 121)) - int(Yn * (44 / 121))))

        return C * Concentration