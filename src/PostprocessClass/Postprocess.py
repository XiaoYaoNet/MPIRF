# coding=UTF-8

from PostprocessClass.Integrationclass.GrayLevel import *
from PostprocessClass.Integrationclass.ThresholdSeg import *

'''
Postprocess.py: The base class of the postprocessing module.
'''

class PostprocessClass(object):
    def __init__(self, DataImage):

        # Convert the objective image to a grayscale image.
        DataImage = (DataImage * 255).round().astype('uint8')

        #call the gray-level histogram component
        self.__GrayLevel=GrayLevelClass(DataImage)

        # call the threshold segmentation component
        self.__ThresholdSeg=ThresholdSegClass(DataImage)

    # Return the result of the gray-level histogram.
    def get_GrayLevel(self):
        return self.__GrayLevel._GrayLevelFunc()

    # Return the result of the threshold segmentation.
    def get_ThresholdSeg(self,thr=150):
        return self.__ThresholdSeg._ThresholdSegFunc(thr)