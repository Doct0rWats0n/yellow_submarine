# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/siri/PycharmProjects/git_projects/yellow_submarine/UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(397, 369)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.circles_button = QtWidgets.QPushButton(self.centralwidget)
        self.circles_button.setGeometry(QtCore.QRect(160, 160, 80, 24))
        self.circles_button.setObjectName("circles_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Круги"))
        self.circles_button.setText(_translate("MainWindow", "Круги"))