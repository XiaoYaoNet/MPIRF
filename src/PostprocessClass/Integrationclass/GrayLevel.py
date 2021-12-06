# coding=UTF-8

import numpy as np

'''
GrayLevel.py: The GrayLevel class realize the function of drawing the gray-level histogram of the reconstruction result image.
'''

class GrayLevelClass(object):
    def __init__(self,ImageData):
        self.ImageData=ImageData

    #Realize drawing gray-scale histogram.
    def _GrayLevelFunc(self):
        x,y=np.shape(self.ImageData)
        H=np.zeros(256)
        for i in range(x):
            for j in range(y):
                H[self.ImageData[i][j]] += 1

        return H