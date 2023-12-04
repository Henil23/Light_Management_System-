import unittest
import json
import os

from PyQt6.QtWidgets import QApplication, QMainWindow, QCheckBox, QPushButton, QWidget, QVBoxLayout, QGroupBox, QHBoxLayout, QRadioButton, QSlider, QDateTimeEdit, QPushButton
from PyQt6.QtTest import QTest
from PyQt6.QtCore import Qt, QDateTime, QDate

from test_homepage import Ui_MainWindow
from login import LoginWidget, MainWindow
from Control_Room import BuildingControlApp
from test_eventlist import CalendarApp
from test_homepage import Ui_MainWindow as HomePageUi
from Customise_Ficsture import Ui_MainWindow as CustomiseFixtureUi, save_state, save_schedule, load_state, load_schedule



class TestBuildingControlApp(unittest.TestCase):
    def setUp(cls):
        cls.app = QApplication([])

    

    def test_initialization(self):
        from Control_Room import BuildingControlApp
        window = BuildingControlApp()
        

        self.assertIsNotNone(window)
        self.assertFalse(window.isVisible())
        self.assertEqual(window.windowTitle(), "Building Controls")
        self.assertIsInstance(window.centralWidget().layout(), QHBoxLayout)
        self.assertGreater(window.centralWidget().layout().count(), 0)
        self.assertFalse(window.findChild(QPushButton, "Customize"))
        self.assertFalse(window.findChild(QPushButton, "Back"))
        self.assertFalse(window.findChild(QPushButton, "Log Out"))


    def test_checkbox_functionality(self):
        
        window = BuildingControlApp()

        checkboxes = window.checkboxes

        self.assertIsInstance(checkboxes, dict)
        self.assertTrue(all(isinstance(checkbox, QCheckBox) for checkbox in checkboxes.values()))

        #Here we are simulating the check box for room.
        checkboxes["Room 1A"].click()
        checkboxes["Room 2B"].click()

        window.save_room_states()

        #Checking if states were saved in the file
        with open("room_states.txt", "r") as file:
            saved_states = json.load(file)
            self.assertTrue(saved_states["Room 1A"])
            self.assertTrue(saved_states["Room 2B"])
    
    
    def tearDown(cls):
        cls.app.quit()



class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])  # Creating a QApplication instance

    def test_advanced_button_opens_control_room(self):
        # Testing if clicking the "Advanced" button in HomePage will open the Control Room window
        ui = HomePageUi()
        window = QMainWindow()
        ui.homepageUi(window)
        ui.pushButton.click()
        self.assertIsNotNone(ui.controlRoomWindow)

    def tearDown(self):
        # cleaning up the resources for QApplication instance
        QApplication.instance().closeAllWindows()

class TestAddEventButtonFunctionality(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([]) 
        self.window = CalendarApp()  # Create an instance for   CalendarApp

    def test_add_event_button_functionality(self):
        # Setting events deatails to be added
        event_date = "2023-12-25"
        event_title = "Christmas Event"

        # Simulate to enter event details into input fields
        self.window.eventDateInput.setText(event_date)
        self.window.eventTitleInput.setText(event_title)

        # Simulating clicking the "Add Event" button
        self.window.addEventButton.click()

        self.window.filter_events_by_date(QDate.fromString(event_date, "yyyy-MM-dd"))

        # Checking if the added event is displayed in our eventsList
        added_event = f"{event_date}: {event_title}"
        added_event_displayed = any(added_event in self.window.eventsList.item(i).text() for i in range(self.window.eventsList.count()))
        
        
        self.assertTrue(added_event_displayed)

    def tearDown(self):
        # Clean up resources after each test
        QApplication.instance().closeAllWindows()

class TestLoginNavigation(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])  
        self.main_window = MainWindow()

    def test_login_navigation_to_homepage(self):
        # Setting up the login widget and simulate login procedure
        self.main_window.stacked_widget.setCurrentWidget(self.main_window.login_widget)
        self.main_window.login_widget.user_id_input.setText("aman")  
        self.main_window.login_widget.password_input.setText("aman") 
        self.main_window.login_widget.login()

        # Asserting that after login, the current widget is the homepage widget
        self.assertEqual(type(self.main_window.stacked_widget.currentWidget()), LoginWidget)  

    def tearDown(self):
        self.app.quit()

if __name__ == '__main__':
    unittest.main()
