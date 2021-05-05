import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui", self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccButton.clicked.connect(self.gotocreate)
        # connects the button with a function

    def loginfunction(self):
        username = self.username.text()
        password = self.password.text()
        #connect with database here
        print("Successfully logged in with username: ", username, "and password :", password)

    def gotocreate(self):
    	createacc = CreateAcc()
    	widget.addWidget(createacc)
    	widget.setCurrentIndex(widget.currentIndex() + 1)	

class CreateAcc(QDialog):
	def __init__(self):
		super(CreateAcc, self).__init__()
		loadUi("Register.ui", self)
		self.signupbutton.clicked.connect(self.createaccfunction)

	def createaccfunction(self):
		username = self.username.text()
		email = self.email.text()
		#connect with database here
		if self.password.text() == self.repeatpassword.text():
			password = self.password.text()
			print("Successfully created an Account with username: ", username, "and password:", password )
			self.diffpasswords.setText("Successfully created an Account!")
			self.username.setReadOnly(True)
			self.password.setReadOnly(True)
			self.repeatpassword.setReadOnly(True)
			self.email.setReadOnly(True)
			self.username.setDisabled(True)
			self.password.setDisabled(True)
			self.repeatpassword.setDisabled(True)
			self.email.setDisabled(True)
		else:
		    self.diffpasswords.setText("Passwords don't match!")

app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(421)
widget.setFixedHeight(721)
widget.show()
app.exec_()