# coding=UTF-8
import numpy as np
from Config.ConstantList import *
from PhantomClass.BassClass.Phantom import *

class EPhantomClass(PhantomClass):
    def __init__(self,Temperature=20.0,Diameter=30e-9,MagSaturation=8e5, Concentration=5e7 ):

        super().__init__(Temperature,
                         Diameter,
                         MagSaturation,
                         Concentration)

    def _get_Picture(self,Concentration,Xn,Yn):
        self._Xn=Xn
        self._Yn=Yn
        C = np.zeros((self._Xn, self._Yn))
        C[int(Xn*(30/201)):int(Xn*(170/201)), int(Yn*(50/201)):int(Yn*(150/201))] = np.ones((int(Xn*(170/201))-int(Xn*(30/201)), int(Yn*(150/201))-int(Yn*(50/201))))
        C[int(Xn*(53/201)):int(Xn*(88/201)), int(Yn*(76/201)):int(Yn*(150/201))] = np.zeros((int(Xn*(88/201))-int(Xn*(53/201)), int(Yn*(150/201))-int(Yn*(76/201))))
        C[int(Xn*(112/201)):int(Xn*(147/201)), int(Yn*(76/201)):int(Yn*(150/201))] = np.zeros((int(Xn*(147/201))-int(Xn*(112/201)), int(Yn*(150/201))-int(Yn*(76/201))))

        return C * Concentration