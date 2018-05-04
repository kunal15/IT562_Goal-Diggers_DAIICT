# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from greedy_ucb import *
global num_ir


class Ui_MainWindoww(object):
    statnum = 0
    givenratin = []
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
        MainWindow.setStyleSheet("QTextEdit#textEdit{\n"
"      color: black;\n"
"   \n"
"}\n"
"\n"
"QTextEdit {\n"
"   \n"
"  color:#4A90E2;\n"
"    font : bold 18px;\n"
"\n"
"}\n"
"\n"
"QCheckBox {\n"
"    spacing: 5px;\n"
"    font: 15px;\n"
"    min-width: 5em;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QPushButton#pushButton {\n"
"    background-color: #4A90E2;\n"
"    font: bold 24px;\n"
"      color: white\n"
"    \n"
"}\n"
"QPushButton#pushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QMainWindow {\n"
"    background: white;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 10, 801, 71))
        self.textEdit.setStyleSheet("QTextEdit #textEdit{\n"
"    \n"
"    padding: 0 8px;\n"
"   \n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(30, 120, 90, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(150, 120, 90, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(250, 120, 90, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(250, 200, 90, 20))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(150, 200, 90, 20))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(30, 200, 90, 20))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_7.setGeometry(QtCore.QRect(250, 280, 90, 20))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_8.setGeometry(QtCore.QRect(150, 280, 90, 20))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_9.setGeometry(QtCore.QRect(30, 280, 90, 20))
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_10.setGeometry(QtCore.QRect(250, 360, 90, 20))
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_11.setGeometry(QtCore.QRect(150, 360, 90, 20))
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_12.setGeometry(QtCore.QRect(30, 360, 90, 20))
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_13 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_13.setGeometry(QtCore.QRect(250, 440, 90, 20))
        self.checkBox_13.setObjectName("checkBox_13")
        self.checkBox_14 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_14.setGeometry(QtCore.QRect(150, 440, 90, 20))
        self.checkBox_14.setObjectName("checkBox_14")
        self.checkBox_15 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_15.setGeometry(QtCore.QRect(30, 440, 90, 20))
        self.checkBox_15.setObjectName("checkBox_15")
        self.checkBox_16 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_16.setGeometry(QtCore.QRect(650, 440, 90, 20))
        self.checkBox_16.setObjectName("checkBox_16")
        self.checkBox_17 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_17.setGeometry(QtCore.QRect(550, 440, 90, 20))
        self.checkBox_17.setObjectName("checkBox_17")
        self.checkBox_18 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_18.setGeometry(QtCore.QRect(430, 440, 90, 20))
        self.checkBox_18.setObjectName("checkBox_18")
        self.checkBox_19 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_19.setGeometry(QtCore.QRect(650, 360, 90, 20))
        self.checkBox_19.setObjectName("checkBox_19")
        self.checkBox_20 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_20.setGeometry(QtCore.QRect(550, 360, 90, 20))
        self.checkBox_20.setObjectName("checkBox_20")
        self.checkBox_21 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_21.setGeometry(QtCore.QRect(430, 360, 90, 20))
        self.checkBox_21.setObjectName("checkBox_21")
        self.checkBox_22 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_22.setGeometry(QtCore.QRect(650, 280, 90, 20))
        self.checkBox_22.setObjectName("checkBox_22")
        self.checkBox_23 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_23.setGeometry(QtCore.QRect(550, 280, 90, 20))
        self.checkBox_23.setObjectName("checkBox_23")
        self.checkBox_24 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_24.setGeometry(QtCore.QRect(430, 280, 90, 20))
        self.checkBox_24.setObjectName("checkBox_24")
        self.checkBox_25 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_25.setGeometry(QtCore.QRect(650, 200, 90, 20))
        self.checkBox_25.setObjectName("checkBox_25")
        self.checkBox_26 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_26.setGeometry(QtCore.QRect(550, 200, 90, 20))
        self.checkBox_26.setObjectName("checkBox_26")
        self.checkBox_27 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_27.setGeometry(QtCore.QRect(430, 200, 90, 20))
        self.checkBox_27.setObjectName("checkBox_27")
        self.checkBox_28 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_28.setGeometry(QtCore.QRect(650, 120, 90, 20))
        self.checkBox_28.setObjectName("checkBox_28")
        self.checkBox_29 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_29.setGeometry(QtCore.QRect(550, 120, 90, 20))
        self.checkBox_29.setObjectName("checkBox_29")
        self.checkBox_30 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_30.setGeometry(QtCore.QRect(430, 120, 90, 20))
        self.checkBox_30.setObjectName("checkBox_30")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 490, 186, 32))
        self.pushButton.setObjectName("pushButton")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 90, 341, 21))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(30, 170, 341, 21))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(30, 250, 341, 21))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(30, 330, 341, 21))
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(30, 410, 341, 21))
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_7 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_7.setGeometry(QtCore.QRect(430, 410, 341, 21))
        self.textEdit_7.setObjectName("textEdit_7")
        self.textEdit_8 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_8.setGeometry(QtCore.QRect(430, 330, 341, 21))
        self.textEdit_8.setObjectName("textEdit_8")
        self.textEdit_9 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_9.setGeometry(QtCore.QRect(430, 250, 341, 21))
        self.textEdit_9.setObjectName("textEdit_9")
        self.textEdit_10 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_10.setGeometry(QtCore.QRect(430, 170, 341, 21))
        self.textEdit_10.setObjectName("textEdit_10")
        self.textEdit_11 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_11.setGeometry(QtCore.QRect(430, 90, 341, 21))
        self.textEdit_11.setObjectName("textEdit_11")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(390, 90, 20, 381))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.setup()
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


    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindo()
        self.ui.setupUi(self.window)
        #close still an issue.
       # self.MainWindow.hide()
        self.window.show()
        self.reload()
    def setup(self):
        #call the method so that recommendation list is updated. 
        x=set([])
        num_ir=0
        start(books)
        print(reco)

        self.textEdit_2.setPlainText(reco[0])
        self.textEdit_3.setPlainText(reco[1])
        self.textEdit_4.setPlainText(reco[2])
        self.textEdit_5.setPlainText(reco[3])
        self.textEdit_6.setPlainText(reco[4])
        self.textEdit_7.setPlainText(reco[9])
        self.textEdit_8.setPlainText(reco[8])
        self.textEdit_9.setPlainText(reco[7])
        self.textEdit_10.setPlainText(reco[6])
        self.textEdit_11.setPlainText(reco[5])

        self.setAllButtonsChecked()
    def reload(self):
        #call the method so that recommendation list is updated. 
        x=set([])
        
        preco = reinforcement_learning(books, greedy_choice_UCB, 2000,Ui_MainWindoww.statnum)
        Ui_MainWindoww.statnum  = Ui_MainWindoww.statnum + 1
        print(preco)
        print(reco)
        self.textEdit_2.setPlainText(preco[0])
        self.textEdit_3.setPlainText(preco[1])
        self.textEdit_4.setPlainText(preco[2])
        self.textEdit_5.setPlainText(preco[3])
        self.textEdit_6.setPlainText(preco[4])
        self.textEdit_7.setPlainText(preco[9])
        self.textEdit_8.setPlainText(preco[8])
        self.textEdit_9.setPlainText(preco[7])
        self.textEdit_10.setPlainText(preco[6])
        self.textEdit_11.setPlainText(preco[5])

        self.setAllButtonsChecked()


    def collect(self):
        num=0
        giv=[]
        if self.checkBox.isChecked():
            num +=1
        else:
            num -=1
        if self.checkBox_2.isChecked():
            num += 3
        if self.checkBox_3.isChecked():
            num -=3
        giv.append(num)
        num=0
        if self.checkBox_6.isChecked():
            num +=1
        else:
            num -=1
        if self.checkBox_5.isChecked():
            num += 3
        if self.checkBox_4.isChecked():
            num -=3
        giv.append(num)
        num=0
        if self.checkBox_9.isChecked():
            num +=1
        else:
            num -=1
        if self.checkBox_8.isChecked():
            num += 3
        if self.checkBox_7.isChecked():
            num -=3
        giv.append(num)
        num=0
        if self.checkBox_12.isChecked():
            num +=1
        else:
            num -=1
        if self.checkBox_11.isChecked():
            num += 3
        if self.checkBox_10.isChecked():
            num -=3
        giv.append(num)
        num=0
        if self.checkBox_15.isChecked():
            num +=1
        else:
            num -=1
        if self.checkBox_14.isChecked():
            num += 3
        if self.checkBox_13.isChecked():
            num -=3
        giv.append(num)
        num=0

        # other side

        if self.checkBox_30.isChecked():
            num +=1
        else:
            num -=1
        if self.checkBox_29.isChecked():
            num += 3
        if self.checkBox_28.isChecked():
            num -=3
        giv.append(num)
        num=0
        if self.checkBox_27.isChecked():
            num +=1
        else:
            num -=1
        if self.checkBox_26.isChecked():
            num += 3
        if self.checkBox_25.isChecked():
            num -=3
        giv.append(num)
        num=0
        if self.checkBox_24.isChecked():
            num +=1
        else:
            num -=1
        if self.checkBox_23.isChecked():
            num += 3
        if self.checkBox_22.isChecked():
            num -=3
        giv.append(num)
        num=0
        if self.checkBox_21.isChecked():
            num +=1
        else:
            num -=1
        if self.checkBox_20.isChecked():
            num += 3
        if self.checkBox_19.isChecked():
            num -=3
        giv.append(num)
        num=0
        if self.checkBox_18.isChecked():
            num +=1
        else:
            num -=1
        if self.checkBox_17.isChecked():
            num += 3
        if self.checkBox_16.isChecked():
            num -=3
        giv.append(num)
        compute_score(giv,Ui_MainWindoww.statnum)
        print(giv)
        giv.clear()
        #from greedy_ucb import givenrating
        #givenrating = [] 
        #givenrating = giv()
        self.reload()



        
        
    def setAllButtonsChecked(self):
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.checkBox_4.setChecked(False)
        self.checkBox_5.setChecked(False)
        self.checkBox_6.setChecked(False)
        self.checkBox_7.setChecked(False)
        self.checkBox_8.setChecked(False)
        self.checkBox_9.setChecked(False)
        self.checkBox_10.setChecked(False)
        self.checkBox_11.setChecked(False)
        self.checkBox_12.setChecked(False)
        self.checkBox_13.setChecked(False)
        self.checkBox_14.setChecked(False)
        self.checkBox_15.setChecked(False)
        self.checkBox_16.setChecked(False)
        self.checkBox_17.setChecked(False)
        self.checkBox_18.setChecked(False)
        self.checkBox_19.setChecked(False)
        self.checkBox_20.setChecked(False)
        self.checkBox_21.setChecked(False)
        self.checkBox_22.setChecked(False)
        self.checkBox_23.setChecked(False)
        self.checkBox_24.setChecked(False)
        self.checkBox_25.setChecked(False)
        self.checkBox_26.setChecked(False)
        self.checkBox_27.setChecked(False)
        self.checkBox_28.setChecked(False)
        self.checkBox_29.setChecked(False)
        self.checkBox_30.setChecked(False)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "recwindow"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:18px; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:40pt; font-weight:400;\">Recommendations</span></p></body></html>"))
        self.checkBox.setText(_translate("MainWindow", "Selected"))
        self.checkBox_2.setText(_translate("MainWindow", "Like"))
        self.checkBox_3.setText(_translate("MainWindow", "Dislike"))
        self.checkBox_4.setText(_translate("MainWindow", "Dislike"))
        self.checkBox_5.setText(_translate("MainWindow", "Like"))
        self.checkBox_6.setText(_translate("MainWindow", "Selected"))
        self.checkBox_7.setText(_translate("MainWindow", "Dislike"))
        self.checkBox_8.setText(_translate("MainWindow", "Like"))
        self.checkBox_9.setText(_translate("MainWindow", "Selected"))
        self.checkBox_10.setText(_translate("MainWindow", "Dislike"))
        self.checkBox_11.setText(_translate("MainWindow", "Like"))
        self.checkBox_12.setText(_translate("MainWindow", "Selected"))
        self.checkBox_13.setText(_translate("MainWindow", "Dislike"))
        self.checkBox_14.setText(_translate("MainWindow", "Like"))
        self.checkBox_15.setText(_translate("MainWindow", "Selected"))
        self.checkBox_16.setText(_translate("MainWindow", "Dislike"))
        self.checkBox_17.setText(_translate("MainWindow", "Like"))
        self.checkBox_18.setText(_translate("MainWindow", "Selected"))
        self.checkBox_19.setText(_translate("MainWindow", "Dislike"))
        self.checkBox_20.setText(_translate("MainWindow", "Like"))
        self.checkBox_21.setText(_translate("MainWindow", "Selected"))
        self.checkBox_22.setText(_translate("MainWindow", "Dislike"))
        self.checkBox_23.setText(_translate("MainWindow", "Like"))
        self.checkBox_24.setText(_translate("MainWindow", "Selected"))
        self.checkBox_25.setText(_translate("MainWindow", "Dislike"))
        self.checkBox_26.setText(_translate("MainWindow", "Like"))
        self.checkBox_27.setText(_translate("MainWindow", "Selected"))
        self.checkBox_28.setText(_translate("MainWindow", "Dislike"))
        self.checkBox_29.setText(_translate("MainWindow", "Like"))
        self.checkBox_30.setText(_translate("MainWindow", "Selected"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

