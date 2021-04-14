# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import  QApplication

from UI.myMainWindow import QmyMainWindow

app = QApplication(sys.argv)

mainform=QmyMainWindow()

mainform.show()

sys.exit(app.exec_())
