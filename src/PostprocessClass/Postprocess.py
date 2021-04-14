# coding=UTF-8

from PostprocessClass.Integrationclass.GrayLevel import *
from PostprocessClass.Integrationclass.ThresholdSeg import *

class PostprocessClass(object):
    def __init__(self, DataImage):
        DataImage = (DataImage * 255).round().astype('uint8')
        self.__GrayLevel=GrayLevelClass(DataImage)
        self.__ThresholdSeg=ThresholdSegClass(DataImage)

    def get_GrayLevel(self):
        return self.__GrayLevel._GrayLevelFunc()

    def get_ThresholdSeg(self,thr=150):
        return self.__ThresholdSeg._ThresholdSegFunc(thr)