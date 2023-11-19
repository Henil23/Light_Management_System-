
from PyQt6.QtWidgets import QApplication, QMainWindow, QCalendarWidget, QPushButton, QLineEdit, QVBoxLayout, QWidget, QListWidget

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
        self.eventsList.addItem(event_string)
        self.eventTitleInput.clear()
        self.eventDateInput.clear()

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

app = QApplication([])
window = CalendarApp()
window.show()
app.exec()

