# coding=UTF-8
import abc

class ReconBaseClass(metaclass=abc.ABCMeta):

    def __init__(self):
        self._ImagSignal=[]

    def get_ImagSiganl(self):
        return self._ImagSignal

    @abc.abstractmethod
    def _ImageRecon(self):pass

    @abc.abstractmethod
    def _ImageReshape(self): pass