# # Developers:

# #################################
# # Henil Patel                   #
# # Muhammad Asim                 # 
# # Amandeep Kaur                 #
# # Sadiya Islam                  #
# # Nischey                       #
# #################################


#importing necessary modules 
import json
import os
from PyQt6 import QtCore, QtGui, QtWidgets
import random
#from Control_Room import BuildingControlApp

# main UI class defined
class Ui_MainWindow(object):


    def homepageUi(self, MainWindow):
        # setting up the main window 
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2432, 1520)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # created various UI elements
        # This is specifically for Energy Widget
        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 151, 463, 228))
        self.listWidget.setObjectName("listWidget")

        # This is responsivle for displaying UI for Alerts where user can write quick notes 
        self.listWidget_2 = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(500, 150, 463, 228))
        self.listWidget_2.setObjectName("listWidget_2")

        # This is used for font for "ENERGY(%)"
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(57, 161, 245, 23))
        self.label.setObjectName("label")

        # This is used for font for "QUICK NOTE"
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(525, 161, 171, 23))
        self.label_2.setObjectName("label_2")


        # self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        # self.label_3.setGeometry(QtCore.QRect(1104, 145, 140, 23))
        # self.label_3.setObjectName("label_3")

        # This is to display calendar widget
        self.calendarWidget = QtWidgets.QCalendarWidget(parent=self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(970, 146, 455, 228))
        self.calendarWidget.setObjectName("calendarWidget")

        # This is used to dislpay the dialog box used to display frequently used fixtures
        self.columnView = QtWidgets.QColumnView(parent=self.centralwidget)
        self.columnView.setGeometry(QtCore.QRect(30, 439, 1400, 300))
        self.columnView.setObjectName("columnView")

        # All the below checkboxes displaying the frequently used Light Fixtures
        # Checkbox 1
        self.checkBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(115, 529, 204, 31))
        self.checkBox.setObjectName("checkBox")
        # Checkbox 2
        self.checkBox_2 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(115, 593, 204, 31))
        self.checkBox_2.setObjectName("checkBox_2")
        # Checkbox 3
        self.checkBox_3 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(568, 529, 204, 31))
        self.checkBox_3.setObjectName("checkBox_3")
        # Checkbox 4
        self.checkBox_4 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(568, 593, 204, 31))
        self.checkBox_4.setObjectName("checkBox_4")
        # Checkbox 5
        self.checkBox_5 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(1054, 529, 204, 31))
        self.checkBox_5.setObjectName("checkBox_5")
        # Checkbox 6
        self.checkBox_6 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(1054, 593, 204, 31))
        self.checkBox_6.setObjectName("checkBox_6")

        # Methods to update the clicked checkboxes in the main Control Room
        self.checkBox.clicked.connect(self.update_room_states)
        self.checkBox_2.clicked.connect(self.update_room_states)
        self.checkBox_3.clicked.connect(self.update_room_states)
        self.checkBox_4.clicked.connect(self.update_room_states)
        self.checkBox_5.clicked.connect(self.update_room_states)
        self.checkBox_6.clicked.connect(self.update_room_states)

        #This is displaying push buttom called "ADVANCED"
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1300, 562, 100, 76))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.open_Control_Room)

        # Displays "FREQUENTLY USED" text 
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(88, 449, 439, 46))
        self.label_4.setObjectName("label_4")
        # It displays the Energy level, it is initialised to 0
        self.lcdNumber = QtWidgets.QLCDNumber(parent=self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(134, 226, 245, 92))
        self.lcdNumber.setProperty("intValue", 00)
        self.lcdNumber.setObjectName("lcdNumber")

        # This function gives the user liberty to write in the NOTES section
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(525, 216, 415, 137))
        self.textEdit.setObjectName("textEdit")

        # It is displaying the iLLumi text on the upper left side
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(32, 18, 269, 76))
        self.label_5.setGeometry(QtCore.QRect(32, 18, 269, 76))
        self.label_5.setObjectName("label_5")

        # displays push button for Log Out
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1368, 38, 90, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.logout)  #function to move the user to Log Out window when clicked

        # Displays "Add Event" button just above the calendar
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(970, 97, 193, 38))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.navigateToEventList)     # function which will move user to Event List when clicked

        # Set the central widget of the main window to the defined central widget
        MainWindow.setCentralWidget(self.centralwidget)
        # Create a menu bar for the main window
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        # Set the geometry (size and position) of the menu bar
        self.menubar.setGeometry(QtCore.QRect(42, 1, 1577, 31))
        # Set the menu bar for the main window
        MainWindow.setMenuBar(self.menubar)
        # Create a status bar for the main window
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        # Set the status bar for the main window
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
          #function to update value which will be displaying in Energy Levels 
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_lcd_number)      
        self.timer.start(5000)      # update the values in every 5 mins
    


    #function that will display numbers in the range of 0-100
    def update_lcd_number(self):
        value = random.randint(50,100)  #values will be displayed between 50-100
        self.lcdNumber.display(value)
        
        
    def showEvent(self, event):
        self.load_checkbox_states()
        super().showEvent(event)

    def focusInEvent(self, event):
        self.load_checkbox_states()
        super().focusInEvent(event)

    #function to update the room states mentioned in Frequently Used section 
    def update_room_states(self):
        states = {
            "Room 1A": self.checkBox.isChecked(),
            "Room 1B": self.checkBox_2.isChecked(),
            "Room 2A": self.checkBox_3.isChecked(),
            "Room 2B": self.checkBox_4.isChecked(),
            "Room 3A": self.checkBox_5.isChecked(),
            "Room 3B": self.checkBox_6.isChecked(),
            # Add the rest of the checkboxes
        }
        with open("room_states.txt", "w") as file:
            json.dump(states, file)

    def update_checkboxes_from_file(self):
        if not os.path.exists("room_states.txt"):
            return
        with open("room_states.txt", "r") as file:
            states = json.load(file)
        for room_name, state in states.items():
            checkbox = getattr(self, room_name.lower().replace(" ", ""), None)
            if checkbox:
                checkbox.setChecked(state)

    def refresh_state(self):
        if not os.path.exists("room_states.txt"):
            return
        with open("room_states.txt", "r") as file:
            states = json.load(file)
        for room_name, state in states.items():
            checkbox = getattr(self, room_name.lower().replace(" ", ""), None)
            if checkbox:
                checkbox.setChecked(state)


    def load_checkbox_states(self):
        if not os.path.exists("room_states.txt"):
            return
        with open("room_states.txt", "r") as file:
            states = json.load(file)
        for room_name, state in states.items():
            checkbox = getattr(self, room_name.lower().replace(" ", ""), None)
            if checkbox:
                checkbox.setChecked(state)


    def open_Control_Room(self):
        from Control_Room import BuildingControlApp
        self.controlRoomWindow = BuildingControlApp()
        self.controlRoomWindow.show()

        
        
 
 # function to navigate to event list
    def navigateToEventList(self):
        from test_eventlist import CalendarApp
        self.eventListWindow = CalendarApp()
        self.eventListWindow.show()

    #function to go back to login page
    def logout(self):
        from login import MainWindow as LoginWindow
        self.login_window = LoginWindow()
        self.login_window.show()
       # QtCore.QCoreApplication.instance().activeWindow().close()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">ENERGY(%):-</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">NOTES:-</span></p></body></html>"))
        self.checkBox.setText(_translate("MainWindow", "ROOM 1A"))
        self.checkBox_2.setText(_translate("MainWindow", "ROOM 1B"))
        self.checkBox_3.setText(_translate("MainWindow", "ROOM 2A"))
        self.checkBox_4.setText(_translate("MainWindow", "ROOM 2B"))
        self.checkBox_5.setText(_translate("MainWindow", "ROOM 3A"))
        self.checkBox_6.setText(_translate("MainWindow", "ROOM 3B"))
        self.pushButton.setText(_translate("MainWindow", "ADVANCED"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:700; font-style:bold;\">FREQUENTLY USED:-</span></p></body></html>"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">1) MEETING IN ROOM 1A</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">2) MAINTAINANCE REQUIRED IN WASHROOM</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">iLLUMi</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "LOGOUT"))
        self.pushButton_3.setText(_translate("MainWindow", "Add Event "))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.homepageUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())



