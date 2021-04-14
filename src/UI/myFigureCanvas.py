##import numpy as np

from PyQt5.QtWidgets import  QWidget

##import matplotlib as mpl
from matplotlib.figure import Figure

from  matplotlib.backends.backend_qt5agg import (FigureCanvas,
            NavigationToolbar2QT as NavigationToolbar)

from PyQt5.QtWidgets import   QVBoxLayout

class QmyFigureCanvas(QWidget):
   
   def __init__(self, parent=None, toolbarVisible=True,showHint=False):
      super().__init__(parent) 

      self.figure=Figure()
      figCanvas = FigureCanvas(self.figure)

      self.naviBar=NavigationToolbar(figCanvas, self)

      actList=self.naviBar.actions()
      count=len(actList)
      self.__lastActtionHint=actList[count-1]
      self.__showHint=showHint
      self.__lastActtionHint.setVisible(self.__showHint)
      
      self.__showToolbar=toolbarVisible
      self.naviBar.setVisible(self.__showToolbar)
      
      layout = QVBoxLayout(self)
      layout.addWidget(self.naviBar)
      layout.addWidget(figCanvas)
      layout.setContentsMargins(0,0,0,0) 
      layout.setSpacing(0) 

      self.__cid=figCanvas.mpl_connect("scroll_event",self.do_scrollZoom)

   def setToolbarVisible(self,isVisible=True):
      self.__showToolbar=isVisible
      self.naviBar.setVisible(isVisible)

   def setDataHintVisible(self,isVisible=True):
      self.__showHint=isVisible
      self.__lastActtionHint.setVisible(isVisible) 
      
   def redraw(self):
      self.figure.canvas.draw()

   def do_scrollZoom(self,event):
      ax=event.inaxes
      if ax==None:
         return
      
      self.naviBar.push_current()
      xmin,xmax=ax.get_xbound()
      xlen=xmax-xmin
      ymin,ymax=ax.get_ybound()
      ylen=ymax-ymin

      xchg=event.step*xlen/20
      xmin=xmin+xchg
      xmax=xmax-xchg
      ychg=event.step*ylen/20
      ymin=ymin+ychg
      ymax=ymax-ychg

      ax.set_xbound(xmin,xmax)
      ax.set_ybound(ymin,ymax)
      event.canvas.draw()