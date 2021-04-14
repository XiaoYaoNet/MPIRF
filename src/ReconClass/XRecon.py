# coding=UTF-8

import numpy as np
from ReconClass.BaseClass.ReconBase import *
from Config.ConstantList import *
from scipy.interpolate import griddata


class XReconClass(ReconBaseClass):

    def __init__(self,Message):
        super().__init__()
        self._ImageRecon(Message)


    def _ImageRecon(self, Message):
        self._ImagSignal.append(self.__XSpace(Message[MEASUREMENT][MEASIGNAL], Message[MEASUREMENT][AUXSIGNAL]))
        self._ImagSignal.append(self._ImageReshape(Message[EXTENDED][RFFP], Message[EXTENDED][FFP],Message[EXTENDED][STEP]))

        return True

    def _ImageReshape(self, Rffp, Ffp, Step):
        pointx = np.arange(min(Rffp[0][:]), max(Rffp[0][:]) + Step, Step)
        pointy = np.arange(min(Rffp[1][:]), max(Rffp[1][:]) + Step, Step)
        xpos, ypos = np.meshgrid(pointx, pointy, indexing='xy')
        ImgTan = griddata((Ffp[0], Ffp[1]), self._ImagSignal[0], (xpos, ypos), method='cubic')

        ImgTan = ImgTan[1:-1, 1:-1]
        ImgTan = ImgTan / np.max(ImgTan)
        return [ImgTan]

    def __XSpace(self,U, Vffp):

        temp = Vffp ** 2
        VffpLen = np.sqrt(temp[0] + temp[1])
        VffpDir = np.divide(Vffp, np.tile(VffpLen, (2, 1)))

        temp = U * VffpDir
        SigTan = temp[0] + temp[1]
        ImgTan = SigTan / VffpLen
        ImgTan = ImgTan / max(ImgTan[:])
        return ImgTan