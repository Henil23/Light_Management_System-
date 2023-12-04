# Developers:

#################################
# Henil Patel                   #
# Muhammad Asim                 # 
# Amandeep Kaur                 #
# Sadiya Islam                  #
# Nischey                       #
#################################

#importing necessary files for unit testing 
import unittest
import json
import os

from PyQt6.QtWidgets import QApplication, QMainWindow, QCheckBox, QPushButton, QWidget, QVBoxLayout, QGroupBox, QHBoxLayout, QRadioButton, QSlider, QDateTimeEdit, QPushButton
from PyQt6.QtTest import QTest
from PyQt6.QtCore import Qt, QDateTime, QDate

from test_homepage import Ui_MainWindow
from Control_Room import BuildingControlApp
from test_eventlist import CalendarApp
from test_homepage import Ui_MainWindow as HomePageUi
from Customise_Ficsture import Ui_MainWindow as CustomiseFixtureUi, save_state, save_schedule, load_state, load_schedule


class TestCustomiseFixture(unittest.TestCase):
    def setUp(cls):
        cls.app = QApplication([])

    
  # Verifying the window closure for the 'Controls' button

    
    def test_save_load_state(self):
        
        # Testing save and load state functionality
        save_state(True, 75)  
        on_state, brightness = load_state() 

        self.assertTrue(on_state)
        self.assertEqual(brightness, 75)

    def test_save_load_schedule(self):
       

        #Testing save and load schedule functionality
        save_schedule(QDateTime.fromString("2023-12-31T23:59:59", "yyyy-MM-ddTHH:mm:ss"))  
        scheduled_datetime = load_schedule()  

        expected_datetime = QDateTime.fromString("2023-12-31T23:59:59", "yyyy-MM-ddTHH:mm:ss")

        self.assertEqual(scheduled_datetime, expected_datetime)

    def tearDown(cls):
        cls.app.quit()


class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])  # Creating a QApplication instance

    def test_adding_event_and_displaying_on_calendar(self):
        # Test adding an event in the CalendarApp and displaying it on the calendar
        window = CalendarApp()
        event_date = "2023-12-25"
        event_title = "Christmas"

        # Add an event
        window.eventDateInput.setText(event_date)
        window.eventTitleInput.setText(event_title)
        window.add_event()

        # Simulate clicking the date on the calendar corresponding to the event
        window.filter_events_by_date(QDate(2023, 12, 25))

        # Check if the added event is displayed in the eventsList
        added_event = f"{event_date}: {event_title}"
        added_event_displayed = any(added_event in window.eventsList.item(i).text() for i in range(window.eventsList.count()))
        self.assertTrue(added_event_displayed)

    def tearDown(self):
        # Clean up resources after each test
        QApplication.instance().closeAllWindows()

if __name__ == '__main__':
    unittest.main()