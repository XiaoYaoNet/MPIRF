# coding=UTF-8

import numpy as np
from Config.ConstantList import *

class ThresholdSegClass(object):
    def __init__(self, ImageData):
        self.ImageData = ImageData

    def _ThresholdSegFunc(self,thr):
        x, y = np.shape(self.ImageData)
        H=np.zeros((x,y))
        for i in range(x):
            for j in range(y):
                if self.ImageData[i][j] > thr:
                    H[i][j] = 1
                else:
                    H[i][j] = 0
        return H