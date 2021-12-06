# coding=UTF-8
import abc

'''
ReconBase.py: The base class of the Image Reconstruction module.
'''

class ReconBaseClass(metaclass=abc.ABCMeta):

    def __init__(self):
        self._ImagSignal=[]

    #Get the image reconstruction result
    def get_ImagSiganl(self):
        return self._ImagSignal

    #Abstract function. Implement image reconstruction algorithm.
    @abc.abstractmethod
    def _ImageRecon(self):pass

    #Abstract function. Resize image.
    @abc.abstractmethod
    def _ImageReshape(self): pass