from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ui import Ui_MainWindow
from telnetlib import EC
from classlinks import GetLinks, OpenLinks
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import json
#  application
app = QtWidgets.QApplication(sys.argv)
# Create form
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

#  ligic
def bp():
    Rule = ui.textEdit.toPlainText()
    Instance= ui.textEdit_2.toPlainText()
    GL = GetLinks()
    GL.main(Rule, Instance)
    OL = OpenLinks()
    OL.main()

    ui.textEdit_2.setText()
ui.pushButton.clicked.connect(bp)


#Run
sys.exit(app.exec_())



