# Developers:

#################################
# Henil Patel                   #
# Muhammad Asim                 # 
# Amandeep Kaur                 #
# Sadiya Islam                  #
# Nischey                       #
#################################


# importing necessary files
from PyQt6 import QtCore, QtGui, QtWidgets
import os
# it loads the random module which contains a number of random number generations related functions
import random
# function that will define the main ui class
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.mainWindow = MainWindow  
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(10000, 10000)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(1150, 375, 2500, 31))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(1370, 375, 250, 31))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(11, 370, 122, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(11, 490, 541, 50))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 91, 70))
        # this pushButton represents Control button in GUI
        self.pushButton.setObjectName("pushButton")
        # function that will close the main window which will move user to Control Room
        self.pushButton.clicked.connect(self.closeMainWindow)
        self.AdjustIntensity = QtWidgets.QSlider(parent=self.centralwidget)
        self.AdjustIntensity.setGeometry(QtCore.QRect(1150, 450, 300, 120))
        self.AdjustIntensity.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.AdjustIntensity.setTickPosition(QtWidgets.QSlider.TickPosition.NoTicks)
        self.AdjustIntensity.setTickInterval(00)
        self.AdjustIntensity.setObjectName("AdjustIntensity")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 370, 120, 470))
        self.label_3.setObjectName("label_3")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(parent=self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(1150, 600, 294, 31))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        # lcdNumber which will represent the power consumption by the fixture
        self.lcdNumber = QtWidgets.QLCDNumber(parent=self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(1200, 245, 151, 31))
        self.lcdNumber.setProperty("intValue", 00) #setting default value to 0
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 260, 301, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 111, 21))
        self.label_5.setObjectName("label_5")
        self.Fixture_Health = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.Fixture_Health.setGeometry(QtCore.QRect(1200, 150, 201, 23))
        self.Fixture_Health.setProperty("value", 98)
        self.Fixture_Health.setObjectName("Fixture_Health")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1350, 10, 91, 70))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.logout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.radioButton.toggled.connect(self.handleLightToggle)
        self.AdjustIntensity.valueChanged.connect(self.handleBrightnessChange)
        self.dateTimeEdit.dateTimeChanged.connect(self.handleScheduleChange)
        #timer to make values change in the power consumed by the fixture
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_LCD_number)
        self.timer.start(15000)

    # function which will update the power consumption 
    def update_LCD_number(self):
        value = random.randint(50,100)
        self.lcdNumber.display(value)        
    # defining the retranslated UI within
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "ON"))
        self.radioButton_2.setText(_translate("MainWindow", "OFF"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:21pt;\">POWER:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:21pt;\">BRIGHTNESS:</span></p><p><br/></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "< CONTROLS"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:21pt;\">SCHEDULE:   </span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:21pt;\">POWER CONSUMPTION: KW/h</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:21pt;\">HEALTH:</span></p><p><span style=\" font-size:18pt;\"><br/></span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "LOG OUT "))
    # this will save state for the brightness level adjustment feature 
    def handleLightToggle(self, checked):
        if checked:
            save_state(True, self.AdjustIntensity.value())
        else:
            save_state(False, self.AdjustIntensity.value())
    
    def handleBrightnessChange(self, value):
        save_state(self.radioButton.isChecked(), value)
    # this will save the state of schedule if changed
    def handleScheduleChange(self, datetime):
        save_schedule(datetime)
    # function to close the main window 
    def closeMainWindow(self):
        """Close the main window."""
        self.mainWindow.close()
    #function to move to login.py window when user chooses to logout 
    def logout (self):
        from login import MainWindow
        self.back = MainWindow()
        self.back.show()
# it will save the states for brightness and schedule in separate txt files
def save_state(on_state, brightness):
    with open("light_state.txt", "w") as file:
        file.write(f"{on_state},{brightness}")

def save_schedule(datetime):
    with open("schedule_state.txt", "w") as file:
        file.write(datetime.toString("yyyy-MM-ddTHH:mm:ss"))

def load_schedule():
    if os.path.exists("schedule_state.txt"):
        with open("schedule_state.txt", "r") as file:
            datetime_str = file.read()
            return QtCore.QDateTime.fromString(datetime_str, "yyyy-MM-ddTHH:mm:ss")
    return QtCore.QDateTime.currentDateTime()

def load_state():
    if os.path.exists("light_state.txt"):
        with open("light_state.txt", "r") as file:
            state = file.read().split(',')
            return state[0] == 'True', int(state[1])
    return False, 50
# executing the GUI
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)  
   # Load saved state and apply it to the UI
    on_state, brightness = load_state()
    ui.radioButton.setChecked(on_state)
    ui.radioButton_2.setChecked(not on_state)
    ui.AdjustIntensity.setValue(brightness)
    scheduled_datetime = load_schedule()
    ui.dateTimeEdit.setDateTime(scheduled_datetime)
    MainWindow.show()
    sys.exit(app.exec())


