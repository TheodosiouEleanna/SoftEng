# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Favorites.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 720)
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 401, 721))
        self.scrollArea.setStyleSheet("background-color: rgb(162, 202, 255);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 399, 719))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.listWidget_3 = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget_3.setGeometry(QtCore.QRect(10, 180, 371, 511))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget_3.setFont(font)
        self.listWidget_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.listWidget_3.setStyleSheet("background-color: rgb(255, 228, 232);\n"
"color: rgb(41, 75, 117);\n"
"\n"
"\n"
"")
        self.listWidget_3.setObjectName("listWidget_3")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        self.Diamoni_10 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Diamoni_10.setGeometry(QtCore.QRect(0, 670, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Diamoni_10.setFont(font)
        self.Diamoni_10.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"background-color: rgb(48, 76, 118);\n"
"color: rgb(255, 255, 255);")
        self.Diamoni_10.setDefault(False)
        self.Diamoni_10.setFlat(False)
        self.Diamoni_10.setObjectName("Diamoni_10")
        self.Diamoni_11 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Diamoni_11.setGeometry(QtCore.QRect(100, 670, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Diamoni_11.setFont(font)
        self.Diamoni_11.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"background-color: rgb(48, 76, 118);\n"
"color: rgb(255, 255, 255);")
        self.Diamoni_11.setDefault(False)
        self.Diamoni_11.setFlat(False)
        self.Diamoni_11.setObjectName("Diamoni_11")
        self.Diamoni_12 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Diamoni_12.setGeometry(QtCore.QRect(200, 670, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Diamoni_12.setFont(font)
        self.Diamoni_12.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"background-color: rgb(48, 76, 118);\n"
"color: rgb(255, 255, 255);")
        self.Diamoni_12.setDefault(False)
        self.Diamoni_12.setFlat(False)
        self.Diamoni_12.setObjectName("Diamoni_12")
        self.Diamoni_13 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Diamoni_13.setGeometry(QtCore.QRect(300, 670, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Diamoni_13.setFont(font)
        self.Diamoni_13.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"background-color: rgb(48, 76, 118);\n"
"color: rgb(255, 255, 255);")
        self.Diamoni_13.setDefault(False)
        self.Diamoni_13.setFlat(False)
        self.Diamoni_13.setObjectName("Diamoni_13")
        self.BOOKALL_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.BOOKALL_2.setGeometry(QtCore.QRect(140, 40, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.BOOKALL_2.setFont(font)
        self.BOOKALL_2.setStyleSheet("background-color: rgb(162, 202, 255);\n"
"color: rgb(27, 36, 156);\n"
"\n"
"")
        self.BOOKALL_2.setObjectName("BOOKALL_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_7.setGeometry(QtCore.QRect(40, 210, 141, 171))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_7.setStyleSheet("color: rgb(41, 75, 117);\n"
"background-color: rgb(206, 255, 217);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_8.setGeometry(QtCore.QRect(210, 210, 141, 171))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_8.setStyleSheet("color: rgb(41, 75, 117);\n"
"background-color: rgb(217, 240, 255);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_9.setGeometry(QtCore.QRect(40, 410, 141, 171))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_9.setStyleSheet("color: rgb(41, 75, 117);\n"
"background-color: rgb(255, 208, 169);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_10.setGeometry(QtCore.QRect(210, 410, 141, 171))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_10.setStyleSheet("color: rgb(41, 75, 117);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setGeometry(QtCore.QRect(40, 610, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.scrollAreaWidgetContents)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(10, 60, 41, 41))
        self.commandLinkButton_3.setText("")
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.Ptiseis_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Ptiseis_3.setGeometry(QtCore.QRect(0, 110, 401, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Ptiseis_3.setFont(font)
        self.Ptiseis_3.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"background-color: rgb(48, 76, 118);\n"
"color: rgb(255, 255, 255);")
        self.Ptiseis_3.setObjectName("Ptiseis_3")
        self.listWidget_3.raise_()
        self.Diamoni_13.raise_()
        self.Diamoni_12.raise_()
        self.Diamoni_11.raise_()
        self.Diamoni_10.raise_()
        self.BOOKALL_2.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.pushButton_10.raise_()
        self.pushButton.raise_()
        self.commandLinkButton_3.raise_()
        self.Ptiseis_3.raise_()
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        __sortingEnabled = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        self.listWidget_3.setSortingEnabled(__sortingEnabled)
        self.Diamoni_10.setText(_translate("Dialog", "Home"))
        self.Diamoni_11.setText(_translate("Dialog", "Search"))
        self.Diamoni_12.setText(_translate("Dialog", "Favorites"))
        self.Diamoni_13.setText(_translate("Dialog", "Profile"))
        self.BOOKALL_2.setText(_translate("Dialog", "BOOKALL"))
        self.pushButton_7.setText(_translate("Dialog", "Favorite 1"))
        self.pushButton_8.setText(_translate("Dialog", "Favorite 2"))
        self.pushButton_9.setText(_translate("Dialog", "Favorite 3"))
        self.pushButton_10.setText(_translate("Dialog", "Favorite 4"))
        self.pushButton.setText(_translate("Dialog", "+ Add More"))
        self.Ptiseis_3.setText(_translate("Dialog", "Favorites"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())