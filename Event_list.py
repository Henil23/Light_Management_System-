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

# Main Application class
class CalendarApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calendar GUI")
        self.setGeometry(100, 100, 800, 600)

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

        self.addEventButton = QPushButton("Add/Update Event", self)
        self.addEventButton.clicked.connect(self.add_event)
        layout.addWidget(self.addEventButton)

        # Add Edit and Delete buttons
        self.editEventButton = QPushButton("Edit Event", self)
        self.editEventButton.clicked.connect(self.edit_event)
        layout.addWidget(self.editEventButton)

        self.deleteEventButton = QPushButton("Delete Event", self)
        self.deleteEventButton.clicked.connect(self.delete_event)
        layout.addWidget(self.deleteEventButton)

        # Add Back button
        self.backButton = QPushButton("Back", self)
        self.backButton.clicked.connect(self.close_application)
        layout.addWidget(self.backButton)

        # Set central widget
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

        # Initialize variable for tracking the currently editing item
        self.currentlyEditingItem = None

        # Load events from file when the application starts
        self.load_events()

    def add_event(self):
        title = self.eventTitleInput.text()
        date = self.eventDateInput.text()
        event_string = f"{date}: {title}"

        if self.currentlyEditingItem:
            # Update the existing event
            self.currentlyEditingItem.setText(event_string)
            self.currentlyEditingItem = None  # Reset the reference
        else:
            # Add a new event
            self.eventsList.addItem(event_string)

        # Clear the input fields after adding or updating an event
        self.eventTitleInput.clear()
        self.eventDateInput.clear()

        # Save the events to the file system
        self.save_all_events()

        # Create EventType and EventData instances for notifications
        event_type = EventType("Calendar Event")
        event_data = EventData(event_string)
        notification = Notification(f"New event added: {event_data.getEventData()} of type {event_type.getEventType()}")
        notification.send()

    def edit_event(self):
        self.currentlyEditingItem = self.eventsList.currentItem()
        if self.currentlyEditingItem:
            date, title = self.currentlyEditingItem.text().split(': ', 1)
            self.eventDateInput.setText(date)
            self.eventTitleInput.setText(title)

    def save_all_events(self):
        events = []
        for index in range(self.eventsList.count()):
            item = self.eventsList.item(index)
            date, title = item.text().split(': ', 1)
            events.append({'date': date, 'title': title})

        with open(EVENTS_FILE, 'w') as f:
            json.dump(events, f)

    def delete_event(self):
        selected_item = self.eventsList.currentItem()
        if selected_item:
            row = self.eventsList.row(selected_item)
            self.eventsList.takeItem(row)
            self.save_all_events()

    def load_events(self):
        if not os.path.exists(EVENTS_FILE):
            return []

        try:
            with open(EVENTS_FILE, 'r') as f:
                events = json.load(f)
            for event in events:
                event_string = f"{event['date']}: {event['title']}"
                self.eventsList.addItem(event_string)
        except json.JSONDecodeError as e:
            print(f"Error reading the JSON file: {e}")
            return []
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return []

    def close_application(self):
        self.close()

# Run the application
if __name__ == "__main__":
    app = QApplication([])
    window = CalendarApp()
    window.show()
    app.exec()
