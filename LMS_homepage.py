

from PyQt6 import QtCore, QtGui, QtWidgets
# from Event_list import CalendarApp



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(649, 501)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 91, 191, 151))
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(210, 90, 191, 151))
        self.listWidget_2.setObjectName("listWidget_2")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 100, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 100, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(430, 90, 58, 16))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.calendarWidget = QtWidgets.QCalendarWidget(parent=self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(410, 88, 231, 151))
        self.calendarWidget.setObjectName("calendarWidget")
        self.columnView = QtWidgets.QColumnView(parent=self.centralwidget)
        self.columnView.setGeometry(QtCore.QRect(20, 270, 621, 181))
        self.columnView.setObjectName("columnView")
        self.checkBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(30, 330, 84, 21))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 370, 84, 21))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(220, 330, 84, 21))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(220, 370, 84, 21))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(410, 330, 84, 21))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(410, 370, 84, 21))
        self.checkBox_6.setObjectName("checkBox_6")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 350, 91, 51))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 280, 181, 31))
        self.label_4.setObjectName("label_4")
        self.lcdNumber = QtWidgets.QLCDNumber(parent=self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(50, 140, 101, 61))
        self.lcdNumber.setProperty("intValue", 90)
        self.lcdNumber.setObjectName("lcdNumber")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(220, 133, 171, 91))
        self.textEdit.setObjectName("textEdit")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 111, 51))
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 20, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 60, 80, 26))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 649, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">ENERGY(%):-</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">ALERTS:-</span></p></body></html>"))
        self.checkBox.setText(_translate("MainWindow", "ROOM 1A"))
        self.checkBox_2.setText(_translate("MainWindow", "ROOM 1B"))
        self.checkBox_3.setText(_translate("MainWindow", "ROOM 2A"))
        self.checkBox_4.setText(_translate("MainWindow", "ROOM 2B"))
        self.checkBox_5.setText(_translate("MainWindow", "ROOM 3A"))
        self.checkBox_6.setText(_translate("MainWindow", "ROOM 3B"))
        self.pushButton.setText(_translate("MainWindow", "ADVANCED"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; font-style:italic;\">FREQUENTLY USED:-</span></p></body></html>"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">1) MEETING IN ROOM 1A</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">2) MAINTAINANCE REQUIRED IN WASHROOM</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">iLLumi</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "LOGUT"))
        self.pushButton_3.setText(_translate("MainWindow", "Add Event "))
        
    #   self.pushButton.clicked.connect(self.advanced_button_clicked)
    #   def advanced_button_clicked(self):
    #         dialog = QDialog(self.centralwidget)
    #         dialog.setWindowTitle("Advanced Options")
    #         dialog.setGeometry(300,300,600,400)
    #         dialog.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
