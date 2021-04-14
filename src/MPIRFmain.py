# coding=UTF-8

from DataClass.Reader.MDFReader import *
from DataClass.Reader.JReader import *
from PreprocessClass.MDFPreprocess import *
from ReconClass.MRecon import *
from matplotlib.pylab import *

from PhantomClass.PPhantom import *
from PhantomClass.EPhantom import *
from DataClass.Scanner.XScanner import *
from ReconClass.XRecon import *

from DataClass.Scanner.MScanner import *

from ReconClass.BaseClass.Imager import *

from PostprocessClass.Postprocess import *

import os

class JsonDefaultEnconding(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, complex):
            return "{real}+{image}i".format(real=o.real, image=o.real)
        if isinstance(o, np.ndarray):
            return o.tolist()

def FileMain(FileType,MsPath,MmPath,MethodType,itera,theta,ThresholdSeg):
    if FileType==0:
        temp = MDFReaderClass(MsPath, MmPath)
        MDFPreprocessClass(temp.Message)
    elif FileType==1:
        temp = JReaderClass(MmPath)
        MDFPreprocessClass(temp.Message)

    if MethodType==0:
        ImgData = MReconClass(temp.Message, itera,np.linalg.norm(temp.Message[MEASUREMENT][AUXSIGNAL], ord='fro') * theta)
    elif MethodType==1:
        ImgData= XReconClass(temp.Message)

    return ImgData.get_ImagSiganl()[1][0], \
           ImgData.get_ImagSiganl()[1][1], \
           ImgData.get_ImagSiganl()[1][2], \
           PostprocessClass(ImgData.get_ImagSiganl()[1][0]).get_GrayLevel(), \
           PostprocessClass(ImgData.get_ImagSiganl()[1][1]).get_GrayLevel(), \
           PostprocessClass(ImgData.get_ImagSiganl()[1][2]).get_GrayLevel(), \
           PostprocessClass(ImgData.get_ImagSiganl()[1][0]).get_ThresholdSeg(ThresholdSeg), \
           PostprocessClass(ImgData.get_ImagSiganl()[1][1]).get_ThresholdSeg(ThresholdSeg), \
           PostprocessClass(ImgData.get_ImagSiganl()[1][2]).get_ThresholdSeg(ThresholdSeg)

def SimulationMain(MethodType,
                   PhanType,Temperature,Diameter,MagSaturation,Concentration,
                   SelectGradietX,SelectGradietY,
                   DriveFrequencyX,DriveFrequencyY,DriveAmplitudeX,DriveAmplitudeY,
                   RepetitionTime,SampleFrequency,
                   Itera,Theta,Delta,ThresholdSeg):

    if PhanType==0:
        phan = PPhantomClass(Temperature,Diameter,MagSaturation,Concentration)
    elif PhanType==1:
        phan = EPhantomClass(Temperature, Diameter, MagSaturation, Concentration)

    if MethodType==0:
        scanner = MScannerClass(phan,
                                SelectGradietX, SelectGradietY,
                                DriveFrequencyX, DriveFrequencyY, DriveAmplitudeX, DriveAmplitudeY,
                                RepetitionTime, SampleFrequency,Delta)

        PreprocessClass(scanner.Message)

        ImgData = MReconClass(scanner.Message,Itera,Theta)

    elif MethodType==1:
        scanner = XScannerClass(phan,
                              SelectGradietX,SelectGradietY,
                              DriveFrequencyX,DriveFrequencyY,DriveAmplitudeX,DriveAmplitudeY,
                              RepetitionTime,SampleFrequency)

        PreprocessClass(scanner.Message)

        ImgData = XReconClass(scanner.Message)

    ResultImage=ImgData.get_ImagSiganl()[1][0]

    return phan.get_PhantomMatrix(), \
           ResultImage, \
           PostprocessClass(ResultImage).get_GrayLevel(), \
           scanner.Message[MEASUREMENT][MEANUMBER][0], \
           scanner.Message[MEASUREMENT][MEANUMBER][1], \
           PostprocessClass(ResultImage).get_ThresholdSeg(ThresholdSeg)

def DelFiles(path_file):
    ls = os.listdir(path_file)
    for i in ls:
        f_path = os.path.join(path_file, i)
        if os.path.isdir(f_path):
            DelFiles(f_path)
        else:
            os.remove(f_path)

if __name__ == "__main__":
    print("*********************************************************")
    print("1: SystemMatrix Reconstruction based on MDF File")
    print("2: SystemMatrix Reconstruction based on Json File")
    print("3: X-Space Reconstruction based on Json File")
    print("4: Simulation of MPI scan based on SystemMatrix")
    print("5: Simulation of MPI scan based on X-Space")
    print("Q: Quit")
    print("*********************************************************")
    instr=''
    instr = input("Please enter the Number: ")
    while not instr=='Q':
        if instr=='1':
            MsPath = input("Please enter the SystemMatrix File Path: ")
            MmPath = input("Please enter the Measurement File Path: ")
            print("Reconstructing...")
            x,y,z,x1,y1,z1,x2,y2,z2 = FileMain(0, MsPath, MmPath, 0, 1, 1, 150)
            DelFiles("./TempImage/")
            ImagerClass.WriteImage(x, "./TempImage/", "XY.jpg")
            ImagerClass.WriteImage(y, "./TempImage/", "XZ.jpg")
            ImagerClass.WriteImage(z, "./TempImage/", "YZ.jpg")
            ImagerClass.WriteImage(x1, "./TempImage/", "XY GrayLevel.jpg")
            ImagerClass.WriteImage(y1, "./TempImage/", "XZ GrayLevel.jpg")
            ImagerClass.WriteImage(z1, "./TempImage/", "YZ GrayLevel.jpg")
            ImagerClass.WriteImage(x2, "./TempImage/", "XY Segmetion.jpg")
            ImagerClass.WriteImage(y2, "./TempImage/", "XZ Segmetion.jpg")
            ImagerClass.WriteImage(z2, "./TempImage/", "YZ Segmetion.jpg")
            print("The result is written into the path:" + os.getcwd() + "/TempImage/")
            break
        elif instr=='2':
            MsPath = None
            MmPath = input("Please enter the JSON File Path: ")
            print("Reconstructing...")
            x,y,z,x1,y1,z1,x2,y2,z2 = FileMain(1, MsPath, MmPath, 0, 1, 1, 150)
            DelFiles("./TempImage/")
            ImagerClass.WriteImage(x, "./TempImage/", "XY.jpg")
            ImagerClass.WriteImage(y, "./TempImage/", "XZ.jpg")
            ImagerClass.WriteImage(z, "./TempImage/", "YZ.jpg")
            ImagerClass.WriteImage(x1, "./TempImage/", "XY GrayLevel.jpg")
            ImagerClass.WriteImage(y1, "./TempImage/", "XZ GrayLevel.jpg")
            ImagerClass.WriteImage(z1, "./TempImage/", "YZ GrayLevel.jpg")
            ImagerClass.WriteImage(x2, "./TempImage/", "XY Segmetion.jpg")
            ImagerClass.WriteImage(y2, "./TempImage/", "XZ Segmetion.jpg")
            ImagerClass.WriteImage(z2, "./TempImage/", "YZ Segmetion.jpg")
            print("The result is written into the path:" + os.getcwd() + "/TempImage/")
            break
        elif instr=='3':
            MsPath = None
            MmPath = input("Please enter the JSON File Path: ")
            print("Reconstructing...")
            x, y, z, x1, y1, z1, x2, y2, z2 = FileMain(1, MsPath, MmPath, 1, 1, 1, 150)
            DelFiles("./TempImage/")
            ImagerClass.WriteImage(x, "./TempImage/", "XY.jpg")
            ImagerClass.WriteImage(y, "./TempImage/", "XZ.jpg")
            ImagerClass.WriteImage(z, "./TempImage/", "YZ.jpg")
            ImagerClass.WriteImage(x1, "./TempImage/", "XY GrayLevel.jpg")
            ImagerClass.WriteImage(y1, "./TempImage/", "XZ GrayLevel.jpg")
            ImagerClass.WriteImage(z1, "./TempImage/", "YZ GrayLevel.jpg")
            ImagerClass.WriteImage(x2, "./TempImage/", "XY Segmetion.jpg")
            ImagerClass.WriteImage(y2, "./TempImage/", "XZ Segmetion.jpg")
            ImagerClass.WriteImage(z2, "./TempImage/", "YZ Segmetion.jpg")
            print("The result is written into the path:" + os.getcwd() + "/TempImage/")
            break
        elif instr=='4':
            print("Use default parameters,Simulating...")
            P,I,G,X,Y,T=SimulationMain(0,0, 20, 30e-9, 8e5, 5e7,
                           2.0, 2.0,
                           2500000.0 / 102.0, 2500000.0 / 96.0, 12e-3, 12e-3,
                           6.528e-4, 2.5e6,
                           1, 1, 5e7, 150)
            DelFiles("./TempImage/")
            ImagerClass.WriteImage(P, "./TempImage/", "Phantom.jpg")
            ImagerClass.WriteImage(I, "./TempImage/", "Reconstruction Result.jpg")
            ImagerClass.WriteImage(G, "./TempImage/", "Threshold Segmetion.jpg")
            ImagerClass.WriteImage(T, "./TempImage/", "GrayLevel histogram.jpg")
            print("The result is written into the path:" + os.getcwd() + "/TempImage/")
            break
        elif instr=='5':
            print("Use default parameters,Simulating...")
            P,I,G,X,Y,T=SimulationMain(1, 0, 20, 30e-9, 8e5, 5e7,
                           2.0, 2.0,
                           2500000.0 / 102.0, 2500000.0 / 96.0, 12e-3, 12e-3,
                           6.528e-4, 2.5e6,
                           1, 1, 5e7, 150)
            DelFiles("./TempImage/")
            ImagerClass.WriteImage(P, "./TempImage/", "Phantom.jpg")
            ImagerClass.WriteImage(I, "./TempImage/", "Reconstruction Result.jpg")
            ImagerClass.WriteImage(G, "./TempImage/", "Threshold Segmetion.jpg")
            ImagerClass.WriteImage(T, "./TempImage/", "GrayLevel histogram.jpg")
            print("The result is written into the path:" + os.getcwd() + "/TempImage/")
            break
        else:
            instr = input("Wrong input, Please re-enter:")