# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dropdown.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(70, 20, 381, 521))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 381, 111))
        self.textEdit.setStyleSheet("background-color:rgb(75, 255, 159)")
        self.textEdit.setObjectName("textEdit")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(120, 60, 113, 20))
        self.lineEdit.setStyleSheet("background-color:rgb(140, 255, 223)")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(300, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 110, 381, 201))
        self.textEdit_2.setStyleSheet("background-color:rgb(255, 245, 202)")
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 110, 121, 41))
        self.pushButton_3.setStyleSheet("background-color:rgb(62, 83, 139)")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 110, 121, 41))
        self.pushButton_4.setStyleSheet("background-color:rgb(62, 83, 139)")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(240, 110, 141, 41))
        self.pushButton_5.setStyleSheet("background-color:rgb(62, 83, 139)")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_10.setGeometry(QtCore.QRect(160, 150, 81, 41))
        self.pushButton_10.setStyleSheet("background-color:rgb(62, 83, 139)")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_11.setGeometry(QtCore.QRect(240, 150, 141, 41))
        self.pushButton_11.setStyleSheet("background-color:rgb(62, 83, 139)")
        self.pushButton_11.setObjectName("pushButton_11")
        self.textEdit_3 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_3.setGeometry(QtCore.QRect(3, 310, 381, 101))
        self.textEdit_3.setStyleSheet("background-color:rgb(255, 245, 202)")
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_4.setGeometry(QtCore.QRect(3, 410, 381, 61))
        self.textEdit_4.setStyleSheet("background-color:rgb(255, 245, 202)")
        self.textEdit_4.setObjectName("textEdit_4")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(0, 150, 161, 161))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setStyleSheet("background-color:rgb(24, 38, 71)")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setStyleSheet("background-color:rgb(24, 38, 71)")
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget)
        self.pushButton_9.setStyleSheet("background-color:rgb(24, 38, 71)")
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout.addWidget(self.pushButton_9)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setStyleSheet("background-color:rgb(24, 38, 71)")
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout.addWidget(self.pushButton_8)
        self.widget1 = QtWidgets.QWidget(self.groupBox)
        self.widget1.setGeometry(QtCore.QRect(0, 490, 381, 25))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_12 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_12.setStyleSheet("background-color:rgb(62, 83, 139)")
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout.addWidget(self.pushButton_12)
        self.pushButton_13 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_13.setStyleSheet("background-color:rgb(62, 83, 139)")
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout.addWidget(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_14.setStyleSheet("background-color:rgb(62, 83, 139)")
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout.addWidget(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_15.setStyleSheet("background-color:rgb(62, 83, 139)")
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout.addWidget(self.pushButton_15)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setText(_translate("MainWindow", "BookAll"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.pushButton_2.setText(_translate("MainWindow", "Background"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                Δραστηριότητες</p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "Διαμονή"))
        self.pushButton_4.setText(_translate("MainWindow", "Πτήσεις"))
        self.pushButton_5.setText(_translate("MainWindow", "Εστίαση"))
        self.pushButton_10.setText(_translate("MainWindow", "Προσφορές"))
        self.pushButton_11.setText(_translate("MainWindow", "Forums"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Προτάσεις για κοντινές δραστηριότητες</p></body></html>"))
        self.textEdit_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Χάρτες</p></body></html>"))
        self.pushButton_6.setText(_translate("MainWindow", "Ξενοδοχεία"))
        self.pushButton_7.setText(_translate("MainWindow", "Air-bnb"))
        self.pushButton_9.setText(_translate("MainWindow", "Motels"))
        self.pushButton_8.setText(_translate("MainWindow", "Camping"))
        self.pushButton_12.setText(_translate("MainWindow", "Home"))
        self.pushButton_13.setText(_translate("MainWindow", "Search"))
        self.pushButton_14.setText(_translate("MainWindow", "Favourites"))
        self.pushButton_15.setText(_translate("MainWindow", "Profile"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
