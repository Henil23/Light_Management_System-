import json
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QGroupBox, QVBoxLayout, QCheckBox, QWidget, QHBoxLayout, QPushButton
from Customise_Ficsture import Ui_MainWindow as setupUI, load_state

class BuildingControlApp(QMainWindow):
    def __init__(self, main_window_ref=None):  # Accept main_window_ref as a parameter
        super().__init__()
        
        self.setWindowTitle("Building Controls")
        self.setGeometry(100, 100, 640, 480)
        self.checkboxes = {}  # Dictionary to store checkbox references

        self.main_window_ref = main_window_ref


        main_layout = QHBoxLayout()
        self.floors = {
            "Floor 1": ["Room 1A", "Room 1B", "Room 1C", "Con. Room", "Washroom"],
            "Floor 2": ["Room 2A", "Room 2B", "Room 2C", "Con. Room", "Washroom"],
            "Floor 3": ["Room 3A", "Room 3B", "Room 3C", "Con. Room", "Washroom"],
            "Floor 4": ["Room 4A", "Room 4B", "Room 4C", "Con. Room", "Washroom"]
        }

        for floor_name, rooms in self.floors.items():
            floor_group_box = self.create_floor_group_box(floor_name, rooms)
            main_layout.addWidget(floor_group_box)

        customize_button = QPushButton("Customize")
        customize_button.clicked.connect(self.open_customise_fixture)
        main_layout.addWidget(customize_button)

        back_button = QPushButton("Back")
        main_layout.addWidget(back_button)
        back_button.clicked.connect(self.backbutton)

        centralWidget = QWidget()
        centralWidget.setLayout(main_layout)
        self.setCentralWidget(centralWidget)

        self.load_checkbox_states()

    def create_floor_group_box(self, floor_name, rooms):
        group_box = QGroupBox(floor_name)
        vbox_layout = QVBoxLayout()

        for room_name in rooms:
            checkbox = QCheckBox(room_name)
            checkbox.setObjectName(room_name)  # Use room name as objectName
            checkbox.clicked.connect(self.save_room_states)
            vbox_layout.addWidget(checkbox)
            self.checkboxes[room_name] = checkbox  # Store the checkbox

        group_box.setLayout(vbox_layout)
        return group_box

    def save_room_states(self):
        print("Saving room states...")
        states = {}
        for room_name, checkbox in self.checkboxes.items():
            states[room_name] = checkbox.isChecked()

        with open("room_states.txt", "w") as file:
            json.dump(states, file)
        if self.main_window_ref:
            self.main_window_ref.refresh_state()

    def load_checkbox_states(self):
        if not os.path.exists("room_states.txt"):
            return
        with open("room_states.txt", "r") as file:
            states = json.load(file)
        for room_name, state in states.items():
            checkbox = self.checkboxes.get(room_name)
            if checkbox:
                checkbox.setChecked(state)


    def showEvent(self, event):
        self.load_checkbox_states()
        super().showEvent(event)

    def focusInEvent(self, event):
        self.load_checkbox_states()
        super().focusInEvent(event)

    def open_customise_fixture(self):
        self.customise_window = QMainWindow()
        self.ui = setupUI()
        self.ui.setupUi(self.customise_window)
        self.customise_window.show()
        on_state, brightness = load_state()
        self.ui.radioButton.setChecked(on_state)
        self.ui.radioButton_2.setChecked(not on_state)
        self.ui.AdjustIntensity.setValue(brightness)

    def backbutton(self):
        self.close()

    def logout(self):
        from login import MainWindow as __init__
        self.logout_window = QMainWindow()
        self.back = __init__(self.logout_window)
        self.logout_window.show()

if __name__ == "__main__":
    app = QApplication([])
    window = BuildingControlApp()
    window.show()
    app.exec()
