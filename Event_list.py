
from PyQt6.QtWidgets import QApplication, QMainWindow, QCalendarWidget, QPushButton, QLineEdit, QVBoxLayout, QWidget, QListWidget
import json
import os

# File to store events
EVENTS_FILE = 'events.json'
# Backend classes
class EventType:
    def __init__(self, event_type):
        self.event_type = event_type

    def getEventType(self):
        return self.event_type


class EventData:
    def __init__(self, event_data):
        self.event_data = event_data

    def getEventData(self):
        return self.event_data


class Notification:
    def __init__(self, content):
        self.content = content

    def getContent(self):
        return self.content

    def send(self):
        # In a real scenario, this method would send the notification
        # For demonstration, we're just printing it
        print(f"Notification: {self.getContent()}")



class CalendarApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calendar GUI")
        self.setGeometry(100, 100, 800, 600)  

        # Load events from file when the application starts
        self.load_events()
        
        layout = QVBoxLayout()

        # Create calendar widget
        self.calendar = QCalendarWidget(self)
        layout.addWidget(self.calendar)
        
        # Create list widget for events
        self.eventsList = QListWidget(self)
        layout.addWidget(self.eventsList)
        
        # Create form to set event
        self.eventTitleInput = QLineEdit(self)
        self.eventTitleInput.setPlaceholderText("Title")
        layout.addWidget(self.eventTitleInput)
        
        self.eventDateInput = QLineEdit(self)
        self.eventDateInput.setPlaceholderText("Date (e.g., 2023-12-24)")
        layout.addWidget(self.eventDateInput)
        
        self.addEventButton = QPushButton("Add Event", self)
        self.addEventButton.clicked.connect(self.add_event)
        layout.addWidget(self.addEventButton)

        # Add Edit and Delete buttons
        self.editEventButton = QPushButton("Edit Event", self)
        self.editEventButton.clicked.connect(self.edit_event)
        layout.addWidget(self.editEventButton)

        self.deleteEventButton = QPushButton("Delete Event", self)
        self.deleteEventButton.clicked.connect(self.delete_event)
        layout.addWidget(self.deleteEventButton)

        self.deleteEventButton = QPushButton("Back", self)
        self.deleteEventButton.clicked.connect(self.delete_event)
        layout.addWidget(self.deleteEventButton)

        # Set central widget
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
    

  
    def add_event(self):
        title = self.eventTitleInput.text()
        date = self.eventDateInput.text()
        event_string = f"{date}: {title}"

        # This is where we add the event to the GUI list
        self.eventsList.addItem(event_string)
        
        # Clear the input fields after adding an event
        self.eventTitleInput.clear()
        self.eventDateInput.clear()

        # Create EventType and EventData instances
        event_type = EventType("Calendar Event")
        event_data = EventData(event_string)

         # Save the event to the file system
        self.save_event(date, title)

        # Now, create a Notification instance
        notification_content = f"New event added: {event_data.getEventData()} of type {event_type.getEventType()}"
        notification = Notification(notification_content)

        # Here we simulate sending the notification
        notification.send()


    def save_event(self, date, title):
        # Load existing events from the file
        events = self.load_events()

        # Add the new event
        events.append({'date': date, 'title': title})

        # Write the updated events back to the file
        with open(EVENTS_FILE, 'w') as f:
            json.dump(events, f)

    def load_events(self):
        # Check if the events file exists
        if not os.path.exists(EVENTS_FILE):
            return []

        # Read the events from the file
        with open(EVENTS_FILE, 'r') as f:
            events = json.load(f)
        
        # Add events to the GUI list
        for event in events:
            event_string = f"{event['date']}: {event['title']}"
            self.eventsList.addItem(event_string)
        
        return events

    def edit_event(self):
        # Get the selected item
        selected_item = self.eventsList.currentItem()
        if selected_item:
            # Split the event string to get the date and title
            date, title = selected_item.text().split(': ', 1)
            self.eventDateInput.setText(date)
            self.eventTitleInput.setText(title)
            # Remove the item from the list
            row = self.eventsList.row(selected_item)
            self.eventsList.takeItem(row)

    def delete_event(self):
        # Get the selected item and remove it
        selected_item = self.eventsList.currentItem()
        if selected_item:
            row = self.eventsList.row(selected_item)
            self.eventsList.takeItem(row)
            # Remove the selected event from the file system
        self.remove_event(selected_item.text())


    def remove_event(self, event_string):
        # Load existing events
        events = self.load_events()

        # Find and remove the event
        events = [event for event in events if f"{event['date']}: {event['title']}" != event_string]

        # Write the updated events back to the file
        with open(EVENTS_FILE, 'w') as f:
            json.dump(events, f)


app = QApplication([])
window = CalendarApp()
window.show()
app.exec()
