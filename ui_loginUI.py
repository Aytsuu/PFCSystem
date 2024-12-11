# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginUIxDAJaY.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc

class Ui_LoginWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setFixedSize(1361, 899)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"background-color: #003910;\n"
"}\n"
"\n"
"#gymName, #gymName_2, #gymName_3, #signInLabel, #userLabel, #passLabel{\n"
"color: #FFFFFF;\n"
"}\n"
"\n"
"#loginForm{\n"
"background-color: rgba(0,57,16,65%);\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"#usernameField, #passwordField{\n"
"border-radius: 10px;\n"
"background-color: #FFFFFF;\n"
"padding: 10px;\n"
"color: #000000;\n"
"}\n"
"\n"
"#signInBtn{\n"
"border-radius: 10px;\n"
"background-color: #77B07D;\n"
"color: white;\n"
"}\n"
"\n"
"#signInBtn:hover{\n"
"background-color: #FFFFFF;\n"
"color: #003910;\n"
"}\n"
"\n"
"#cl1{\n"
"border-radius: 10px;\n"
"background-color: #D60000;\n"
"}\n"
"\n"
"#cl2{\n"
"border-radius: 10px;\n"
"background-color: #00E217;\n"
"}\n"
"\n"
"#cl3{\n"
"border-radius: 10px;\n"
"background-color: #FAD30A;\n"
"}")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(500, -10, 921, 911))
        self.bgLogin = QLabel(self.widget)
        self.bgLogin.setObjectName(u"bgLogin")
        self.bgLogin.setGeometry(QRect(-90, 0, 1401, 921))
        self.bgLogin.setPixmap(QPixmap(u":/loginRES/42a5b706fb93fb17337d4cbf2eab49ec.jpg"))
        self.bgLogin.setScaledContents(True)
        self.loginForm = QWidget(self.widget)
        self.loginForm.setObjectName(u"loginForm")
        self.loginForm.setGeometry(QRect(220, 180, 441, 531))
        self.loginForm.setStyleSheet(u"")
        self.signInLabel = QLabel(self.loginForm)
        self.signInLabel.setObjectName(u"signInLabel")
        self.signInLabel.setGeometry(QRect(160, 60, 121, 51))
        font = QFont()
        font.setFamily(u"Yu Gothic UI Semibold")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setLegacyWeight(75)
        self.signInLabel.setFont(font)
        self.userLabel = QLabel(self.loginForm)
        self.userLabel.setObjectName(u"userLabel")
        self.userLabel.setGeometry(QRect(60, 150, 121, 31))
        font1 = QFont()
        font1.setFamily(u"Yu Gothic UI Semibold")
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setLegacyWeight(75)
        self.userLabel.setFont(font1)
        self.passLabel = QLabel(self.loginForm)
        self.passLabel.setObjectName(u"passLabel")
        self.passLabel.setGeometry(QRect(60, 280, 121, 31))
        self.passLabel.setFont(font1)
        self.signInBtn = QPushButton(self.loginForm)
        self.signInBtn.setObjectName(u"signInBtn")
        self.signInBtn.setGeometry(QRect(160, 430, 121, 41))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(119, 176, 125, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 128))
        brush2.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush3 = QBrush(QColor(255, 255, 255, 128))
        brush3.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush4 = QBrush(QColor(255, 255, 255, 128))
        brush4.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.signInBtn.setPalette(palette)
        font2 = QFont()
        font2.setFamily(u"Yu Gothic UI Semibold")
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setLegacyWeight(75)
        self.signInBtn.setFont(font2)
        self.signInBtn.setCursor(QCursor(Qt.ArrowCursor))
        self.usernameField = QLineEdit(self.loginForm)
        self.usernameField.setObjectName(u"usernameField")
        self.usernameField.setGeometry(QRect(60, 200, 321, 40))
        font3 = QFont()
        font3.setFamily(u"Yu Gothic UI")
        font3.setPointSize(10)
        self.usernameField.setFont(font3)
        self.usernameField.setStyleSheet(u"")
        self.usernameField.setFrame(True)
        self.usernameField.setCursorPosition(0)
        self.passwordField = QLineEdit(self.loginForm)
        self.passwordField.setObjectName(u"passwordField")
        self.passwordField.setGeometry(QRect(60, 330, 321, 40))
        font4 = QFont()
        font4.setFamily(u"Yu Gothic UI")
        font4.setPointSize(8)
        font4.setKerning(True)
        self.passwordField.setFont(font4)
        self.passwordField.setStyleSheet(u"")
        self.passwordField.setEchoMode(QLineEdit.Password)
        self.passwordField.setDragEnabled(False)
        self.signInBtn.raise_()
        self.signInLabel.raise_()
        self.userLabel.raise_()
        self.passLabel.raise_()
        self.usernameField.raise_()
        self.passwordField.raise_()
        self.gymName = QLabel(self.centralwidget)
        self.gymName.setObjectName(u"gymName")
        self.gymName.setGeometry(QRect(90, 460, 311, 51))
        font5 = QFont()
        font5.setFamily(u"Yu Gothic UI Semibold")
        font5.setPointSize(30)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setLegacyWeight(75)
        self.gymName.setFont(font5)
        self.gymName_2 = QLabel(self.centralwidget)
        self.gymName_2.setObjectName(u"gymName_2")
        self.gymName_2.setGeometry(QRect(170, 520, 151, 51))
        self.gymName_2.setFont(font5)
        self.gymName_3 = QLabel(self.centralwidget)
        self.gymName_3.setObjectName(u"gymName_3")
        self.gymName_3.setGeometry(QRect(200, 820, 111, 51))
        font6 = QFont()
        font6.setFamily(u"Yu Gothic UI Semibold")
        font6.setPointSize(20)
        font6.setBold(True)
        font6.setItalic(False)
        font6.setLegacyWeight(75)
        self.gymName_3.setFont(font6)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 180, 211, 201))
        self.label.setStyleSheet(u"border-image: url(:/loginRES/logo.png);\n"
"border-radius:100px;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bgLogin.setText("")
        self.signInLabel.setText(QCoreApplication.translate("MainWindow", u"SIGN IN", None))
        self.userLabel.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.passLabel.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.signInBtn.setText(QCoreApplication.translate("MainWindow", u"LOG IN", None))
        self.usernameField.setText("")
        self.passwordField.setText("")
        self.gymName.setText(QCoreApplication.translate("MainWindow", u"PEOPLE FITNESS", None))
        self.gymName_2.setText(QCoreApplication.translate("MainWindow", u"CENTER", None))
        self.gymName_3.setText(QCoreApplication.translate("MainWindow", u"EST 2006", None))
        self.label.setText("")
    # retranslateUi

