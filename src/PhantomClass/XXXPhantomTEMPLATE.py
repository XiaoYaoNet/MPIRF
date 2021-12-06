# coding=UTF-8

from PhantomClass.BassClass.Phantom import *

'''
This is a template file.
'''

class XXXPhantomClass(PhantomClass):
    def __init__(self,Temperature=20.0,Diameter=30e-9,MagSaturation=8e5, Concentration=5e7 ):

        super().__init__(Temperature,
                         Diameter,
                         MagSaturation,
                         Concentration)

    def get_Phantom(self,Concentration,Xn,Yn):
        C = np.zeros((self.Xn, self.Yn))

        #TODO: add your virtual phantom shape code

        return C * Concentration