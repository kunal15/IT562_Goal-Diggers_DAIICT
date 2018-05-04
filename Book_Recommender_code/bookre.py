# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BookRec.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from rect import Ui_MainWindoww
from greedy_ucb import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QTextEdit {\n"
"    padding: 0 8px;\n"
"    font-size: 100px;\n"
"    selection-background-color: yellow;\n"
"    background-color : #4A90E2;\n"
"    padding: 0 8px;\n"
"    font-size: 30px;\n"
"}\n"
"QTextEdit#textEdit{\n"
"    background-color : white;\n"
"    padding: 0 8px;\n"
"    font-size: 30px;\n"
"\n"
"    \n"
"    \n"
"  \n"
"}\n"
"QCheckBox {\n"
"    spacing: 5px;\n"
"    \n"
"    font:20px;\n"
"    min-width: 8em;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    solid : red;\n"
"}\n"
"\n"
"QPushButton#pushButton {\n"
"    background-color: #4A90E2;\n"
"    font: bold 24px;\n"
"    color: white;\n"
"    padding: 2px;\n"
"}\n"
"QPushButton#pushButton:pressed {\n"
"    background-color: yellow;\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QMainWindow {\n"
"    background: white;\n"
"}\n"
"\n"
"")
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(-110, 0, 991, 101))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(-10, 90, 1061, 41))
        self.textEdit_2.setStyleSheet("QTextEdit#textEdit2{\n"
"    border: 3px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    font-size: 100px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.textEdit_2.setObjectName("textEdit_2")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 170, 230, 21))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 200, 230, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 230, 230, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(20, 260, 230, 20))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(20, 290, 230, 20))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(20, 320, 230, 20))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_7.setGeometry(QtCore.QRect(20, 350, 230, 20))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_8.setGeometry(QtCore.QRect(20, 380, 230, 20))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_9.setGeometry(QtCore.QRect(20, 410, 230, 20))
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_10.setGeometry(QtCore.QRect(280, 170, 230, 20))
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_11.setGeometry(QtCore.QRect(280, 200, 230, 20))
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_12.setGeometry(QtCore.QRect(280, 230, 230, 20))
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_13 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_13.setGeometry(QtCore.QRect(280, 260, 230, 20))
        self.checkBox_13.setObjectName("checkBox_13")
        self.checkBox_14 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_14.setGeometry(QtCore.QRect(280, 290, 230, 20))
        self.checkBox_14.setObjectName("checkBox_14")
        self.checkBox_15 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_15.setGeometry(QtCore.QRect(280, 320, 230, 20))
        self.checkBox_15.setObjectName("checkBox_15")
        self.checkBox_16 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_16.setGeometry(QtCore.QRect(280, 350, 230, 20))
        self.checkBox_16.setObjectName("checkBox_16")
        self.checkBox_17 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_17.setGeometry(QtCore.QRect(280, 380, 230, 20))
        self.checkBox_17.setObjectName("checkBox_17")
        self.checkBox_18 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_18.setGeometry(QtCore.QRect(280, 410, 230, 20))
        self.checkBox_18.setObjectName("checkBox_18")
        self.checkBox_19 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_19.setGeometry(QtCore.QRect(540, 170, 230, 20))
        self.checkBox_19.setObjectName("checkBox_19")
        self.checkBox_20 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_20.setGeometry(QtCore.QRect(540, 200, 230, 20))
        self.checkBox_20.setObjectName("checkBox_20")
        self.checkBox_21 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_21.setGeometry(QtCore.QRect(540, 230, 230, 20))
        self.checkBox_21.setObjectName("checkBox_21")
        self.checkBox_22 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_22.setGeometry(QtCore.QRect(540, 260, 230, 20))
        self.checkBox_22.setObjectName("checkBox_22")
        self.checkBox_23 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_23.setGeometry(QtCore.QRect(540, 290, 230, 20))
        self.checkBox_23.setObjectName("checkBox_23")
        self.checkBox_24 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_24.setGeometry(QtCore.QRect(540, 320, 230, 20))
        self.checkBox_24.setObjectName("checkBox_24")
        self.checkBox_25 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_25.setGeometry(QtCore.QRect(540, 350, 230, 20))
        self.checkBox_25.setObjectName("checkBox_25")
        self.checkBox_26 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_26.setGeometry(QtCore.QRect(540, 380, 230, 20))
        self.checkBox_26.setObjectName("checkBox_26")
        self.checkBox_27 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_27.setGeometry(QtCore.QRect(540, 410, 230, 20))
        self.checkBox_27.setObjectName("checkBox_27")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 470, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.collect)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def collect(self):
        if self.checkBox.isChecked():
            gl.append(0)
        if self.checkBox_2.isChecked():
            gl.append(1)
        if self.checkBox_3.isChecked():
            gl.append(2)
        if self.checkBox_4.isChecked():
            gl.append(3)
        if self.checkBox_5.isChecked():
            gl.append(4)
        if self.checkBox_6.isChecked():
            gl.append(5)
        if self.checkBox_7.isChecked():
            gl.append(6)
        if self.checkBox_8.isChecked():
            gl.append(7)
        if self.checkBox_9.isChecked():
            gl.append(8)
        if self.checkBox_10.isChecked():
            gl.append(9)
        if self.checkBox_11.isChecked():
            gl.append(10)
        if self.checkBox_12.isChecked():
            gl.append(11)
        if self.checkBox_13.isChecked():
            gl.append(12)
        if self.checkBox_14.isChecked():
            gl.append(13)
        if self.checkBox_15.isChecked():
            gl.append(14)
        if self.checkBox_16.isChecked():
            gl.append(15)
        if self.checkBox_17.isChecked():
            gl.append(16)
        if self.checkBox_18.isChecked():
            gl.append(17)
        if self.checkBox_19.isChecked():
            gl.append(18)
        if self.checkBox_20.isChecked():
            gl.append(19)
        if self.checkBox_21.isChecked():
            gl.append(20)
        if self.checkBox_22.isChecked():
            gl.append(21)
        if self.checkBox_23.isChecked():
            gl.append(22)
        if self.checkBox_24.isChecked():
            gl.append(23)
        if self.checkBox_25.isChecked():
            gl.append(24)
        if self.checkBox_26.isChecked():
            gl.append(25)
        if self.checkBox_27.isChecked():
            gl.append(26)
        print(gl)
        
        self.openWindow()


    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindoww()
        self.ui.setupUi(self.window)
        MainWindow.close()
        self.window.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto\'; font-size:30px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48px;\">    BOOK RECOMMENDER 📖</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:30px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#fefefe;\">     Choose Your Genre</span></p></body></html>"))
        self.checkBox.setText(_translate("MainWindow", "Fantasy"))
        self.checkBox_2.setText(_translate("MainWindow", "Art"))
        self.checkBox_3.setText(_translate("MainWindow", "Biography"))
        self.checkBox_4.setText(_translate("MainWindow", "Business"))
        self.checkBox_5.setText(_translate("MainWindow", "Christian"))
        self.checkBox_6.setText(_translate("MainWindow", "Classics"))
        self.checkBox_7.setText(_translate("MainWindow", "Comics"))
        self.checkBox_8.setText(_translate("MainWindow", "Cookbooks"))
        self.checkBox_9.setText(_translate("MainWindow", "Crime"))
        self.checkBox_10.setText(_translate("MainWindow", "History"))
        self.checkBox_11.setText(_translate("MainWindow", "Horror"))
        self.checkBox_12.setText(_translate("MainWindow", "Manga"))
        self.checkBox_13.setText(_translate("MainWindow", "Memoir"))
        self.checkBox_14.setText(_translate("MainWindow", "Music"))
        self.checkBox_15.setText(_translate("MainWindow", "Mystery"))
        self.checkBox_16.setText(_translate("MainWindow", "Paranormal"))
        self.checkBox_17.setText(_translate("MainWindow", "Philosophy"))
        self.checkBox_18.setText(_translate("MainWindow", "Poetry"))
        self.checkBox_19.setText(_translate("MainWindow", "Psychology"))
        self.checkBox_20.setText(_translate("MainWindow", "Religion"))
        self.checkBox_21.setText(_translate("MainWindow", "Romance"))
        self.checkBox_22.setText(_translate("MainWindow", "Science"))
        self.checkBox_23.setText(_translate("MainWindow", "Spirituality"))
        self.checkBox_24.setText(_translate("MainWindow", "Sports"))
        self.checkBox_25.setText(_translate("MainWindow", "Suspense"))
        self.checkBox_26.setText(_translate("MainWindow", "Thriller"))
        self.checkBox_27.setText(_translate("MainWindow", "Travel"))
        self.pushButton.setText(_translate("MainWindow", "SUBMIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

