# -*- coding: utf-8 -*-

import sys, random

import matplotlib.pyplot as plt
import numpy as np

from Config.UIConstantListEn import *
#from Config.UIConstantList import *

from PyQt5.QtWidgets import  QApplication, QMainWindow,QFileDialog

from PyQt5.QtCore import  Qt,pyqtSlot

from UI.ui_MainWindow import Ui_MainWindow

from PyQt5 import QtCore

from MPIRFmain import *


class QmyMainWindow(QMainWindow):

   def __init__(self, parent=None):
      super().__init__(parent)
      self.ui=Ui_MainWindow()
      self.ui.setupUi(self)

      self._translate = QtCore.QCoreApplication.translate

      self.setWindowTitle(TITLE)
      pass

   def __drawHist(self, FileType,MsPath,MmPath,MethodIndex,itera,theta,thresholdseg):

      x,y,z,x1,y1,z1,x2,y2,z2=FileMain(FileType,MsPath,MmPath,MethodIndex,itera,theta,thresholdseg)

      self.ui.chartViewBar.figure.clear()
      if not x is None:
          ax1 = self.ui.chartViewBar.figure.add_subplot(3, 3, 1, label="points")
          ax1.imshow(x)
          ax1.set_title("X-Y")

      if not y is None:
         ax2 = self.ui.chartViewBar.figure.add_subplot(3, 3, 2, label="points")
         ax2.imshow(y)
         ax2.set_title("X-Z")

      if not z is None:
         ax3 = self.ui.chartViewBar.figure.add_subplot(3, 3, 3, label="points")
         ax3.imshow(z)
         ax3.set_title("Y-Z")
         sp = ax3.scatter(z[:], z[:], c=z[:])
         self.ui.chartViewBar.figure.colorbar(sp)
      else:
         sp = ax1.scatter(x[:], x[:], c=x[:])
         self.ui.chartViewBar.figure.colorbar(sp)

      if not x1 is None:
          ax4 = self.ui.chartViewBar.figure.add_subplot(3, 3, 4, label="points")
          ax4.bar(range(256), x1, color="blue")
          ax4.set_title("Gray-level Histogram")

      if not y1 is None:
          ax5 = self.ui.chartViewBar.figure.add_subplot(3, 3, 5, label="points")
          ax5.bar(range(256), y1, color="blue")
          ax5.set_title("Gray-level Histogram")

      if not z1 is None:
          ax6 = self.ui.chartViewBar.figure.add_subplot(3, 3, 6, label="points")
          ax6.bar(range(256), z1, color="blue")
          ax6.set_title("Gray-level Histogram")

      if not x2 is None:
          ax7 = self.ui.chartViewBar.figure.add_subplot(3, 3, 7, label="points")
          ax7.imshow(x2)
          ax7.set_title("Threshold Segmation")

      if not y2 is None:
         ax8 = self.ui.chartViewBar.figure.add_subplot(3, 3, 8, label="points")
         ax8.imshow(y2)
         ax8.set_title("Threshold Segmation")

      if not z2 is None:
         ax9 = self.ui.chartViewBar.figure.add_subplot(3, 3, 9, label="points")
         ax9.imshow(z2)
         ax9.set_title("Threshold Segmation")

      self.ui.chartViewBar.figure.subplots_adjust(hspace=0.6, wspace=0.5)

      self.ui.lableresult1.setText(IMAGESIZE + str(np.shape(x)[0]) + "X" + str(np.shape(x)[1]))

   def __drawHist2(self,
                   MethodType,
                   PhanType,
                   Temperature,
                   Diameter,
                   MagSaturation,
                   Concentration,
                   SelectGradietX,
                   SelectGradietY,
                   DriveFrequencyX,
                   DriveFrequencyY,
                   DriveAmplitudeX,
                   DriveAmplitudeY,
                   RepetitionTime,
                   SampleFrequency,
                   Itera,
                   Theta,
                   Delta,
                   ThresholdSeg):

      x,y,z,xn,yn, seg=SimulationMain(MethodType,
                                 PhanType,
                                 Temperature,
                                 Diameter,
                                 MagSaturation,
                                 Concentration,
                                 SelectGradietX,
                                 SelectGradietY,
                                 DriveFrequencyX,
                                 DriveFrequencyY,
                                 DriveAmplitudeX,
                                 DriveAmplitudeY,
                                 RepetitionTime,
                                 SampleFrequency,
                                 Itera,
                                 Theta,
                                 Delta,
                                 ThresholdSeg)

      self.ui.chartViewPie.figure.clear()
      ax1 = self.ui.chartViewPie.figure.add_subplot(2, 4, 1, label="points")
      ax1.imshow(x)
      ax1.set_title("Virtual Phantom")

      ax2 = self.ui.chartViewPie.figure.add_subplot(2, 4, 2, label="points")
      ax2.imshow(y)
      ax2.set_title("Reconstructed Image")
      # sp=ax3.scatter(y[:],y[:],c=y[:],cmap='Greens')
      sp = ax2.scatter(y[:], y[:], c=y[:])
      self.ui.chartViewPie.figure.colorbar(sp)

      ax3 = self.ui.chartViewPie.figure.add_subplot(2, 4, 3, label="points")
      ax3.bar(range(256), z, color="blue")
      ax3.set_title("Gray-level Histogram")
      self.ui.chartViewPie.figure.subplots_adjust(hspace=0.4,wspace=0.5)

      ax4 = self.ui.chartViewPie.figure.add_subplot(2, 4, 4, label="points")
      ax4.imshow(seg)
      ax4.set_title("Threshold Segmation")

      self.ui.lableresult2.setText(IMAGESIZE +str(xn)+"X"+str(yn))

   @pyqtSlot()
   def on_btnBuildBarChart_clicked(self):
      get_filename_path, ok = QFileDialog.getOpenFileName(self,
                                                          "select a file",
                                                          "C:/",
                                                          "All Files (*);;Text Files (*.txt)")
      if ok:
         self.ui.btnBuildBarEditMS.setText(str(get_filename_path))

   @pyqtSlot()
   def on_btnBuildBarChartH_clicked(self):
      get_filename_path, ok = QFileDialog.getOpenFileName(self,
                                                          "select a file",
                                                          "C:/",
                                                          "All Files (*);;Text Files (*.txt)")
      if ok:
         self.ui.btnBuildBarEditMM.setText(str(get_filename_path))

   @pyqtSlot()
   def on_btnBuildBarChartS_clicked(self):
      itera=int(self.ui.btnIteration.text())
      theta=float(self.ui.btnTheta.text())
      thresholdseg = int(self.ui.btnTheta5.text())
      self.__drawHist(self.ui.comboFile.currentIndex(),
                      self.ui.btnBuildBarEditMS.text(),
                      self.ui.btnBuildBarEditMM.text(),
                      self.ui.comboMethod.currentIndex(),
                      itera,
                      theta,
                      thresholdseg)
      self.ui.chartViewBar.redraw()

   @pyqtSlot(int)
   def on_comboFile_currentIndexChanged(self, index):
      if index == 0:
         # self.ui.btnBuildBarChartH.setText(self._translate("MainWindow", "选择MDF测量文件"))
         self.ui.btnBuildBarChart.setVisible(True)
         self.ui.btnBuildBarEditMS.setVisible(True)
         self.ui.label0_S1.setVisible(True)
         self.ui.btnBuildBarEditMM.setText("")
      elif index == 1:
         # self.ui.btnBuildBarChartH.setText(self._translate("MainWindow", "选择Json测量文件"))
         self.ui.btnBuildBarChart.setVisible(False)
         self.ui.btnBuildBarEditMS.setVisible(False)
         self.ui.label0_S1.setVisible(False)
         self.ui.btnBuildBarEditMM.setText("")

   @pyqtSlot(int)
   def on_comboMethod_currentIndexChanged(self, index):
      if index == 0:
         self.ui.label31.setVisible(True)
         self.ui.label32.setVisible(True)
         self.ui.btnIteration.setVisible(True)
         self.ui.btnTheta.setVisible(True)
      elif index == 1:
         self.ui.label31.setVisible(False)
         self.ui.label32.setVisible(False)
         self.ui.btnIteration.setVisible(False)
         self.ui.btnTheta.setVisible(False)

   @pyqtSlot(int)
   def on_comboMethod2_currentIndexChanged(self, index):
      if index == 0:
         self.ui.label231.setVisible(True)
         self.ui.label232.setVisible(True)
         self.ui.label233.setVisible(True)
         self.ui.btnDelta2.setVisible(True)
         self.ui.btnIteration2.setVisible(True)
         self.ui.btnTheta2.setVisible(True)
         self.ui.label234.setVisible(True)
      elif index == 1:
         self.ui.label231.setVisible(False)
         self.ui.label232.setVisible(False)
         self.ui.btnIteration2.setVisible(False)
         self.ui.btnTheta2.setVisible(False)
         self.ui.label233.setVisible(False)
         self.ui.btnDelta2.setVisible(False)
         self.ui.label234.setVisible(False)
      
   @pyqtSlot()
   def on_btnDrawPieChart_clicked(self):
      MethodType=self.ui.comboMethod2.currentIndex()
      PhanType=self.ui.comboCourse.currentIndex()

      Temperature=float(self.ui.pieEdit_2.text())
      Diameter=float(self.ui.pieEdit_3.text())*1e-9
      MagSaturation=float(self.ui.pieEdit_4.text())*1e3
      Concentration=float(self.ui.pieEdit_5.text())*1e-3

      SelectGradietX=float(self.ui.pieEdit2_2.text())
      SelectGradietY=float(self.ui.pieEdit3_2.text())
      DriveFrequencyX=float(self.ui.pieEdit4_2.text())*1e3
      DriveFrequencyY=float(self.ui.pieEdit5_2.text())*1e3
      DriveAmplitudeX=float(self.ui.pieEdit6_2.text())*1e-3
      DriveAmplitudeY=float(self.ui.pieEdit7_2.text())*1e-3
      RepetitionTime=float(self.ui.pieEdit8_2.text())*1e-6
      SampleFrequency=float(self.ui.pieEdit9_2.text())*1e6

      Iterations=int(self.ui.btnIteration2.text())
      Theta=float(self.ui.btnTheta2.text())
      Delta=float(self.ui.btnDelta2.text())
      ThresholdSeg=int(self.ui.btnDelta3.text())

      self.__drawHist2(MethodType,
                       PhanType,
                       Temperature,
                       Diameter,
                       MagSaturation,
                       Concentration,
                       SelectGradietX,
                       SelectGradietY,
                       DriveFrequencyX,
                       DriveFrequencyY,
                       DriveAmplitudeX,
                       DriveAmplitudeY,
                       RepetitionTime,
                       SampleFrequency,
                       Iterations,
                       Theta,
                       Delta,
                       ThresholdSeg)
      self.ui.chartViewPie.redraw()
