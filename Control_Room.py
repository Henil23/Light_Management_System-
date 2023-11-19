import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QGroupBox, QVBoxLayout, QCheckBox, QLabel, QWidget, QHBoxLayout)

class BuildingControlApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Building Controls")
        self.setGeometry(100, 100, 640, 480)  

        # Define the layout for the central widget
        main_layout = QHBoxLayout()
        
        # Create group boxes for each floor
        floors = {
            "Floor 1": ["Room 1A", "Room 1B", "Room 1C", "Con. Room", "Washroom"],
            "Floor 2": ["Room 2A", "Room 2B", "Room 2C", "Con. Room", "Washroom"],
            "Floor 3": ["Room 3A", "Room 3B", "Room 3C", "Con. Room", "Washroom"],
            "Floor 4": ["Room 4A", "Room 4B", "Room 4C", "Con. Room", "Washroom"]
        }
        
        # Create the GUI components for each floor
        for floor_name, rooms in floors.items():
            floor_group_box = self.create_floor_group_box(floor_name, rooms)
            main_layout.addWidget(floor_group_box)

        # Set central widget
        centralWidget = QWidget()
        centralWidget.setLayout(main_layout)
        self.setCentralWidget(centralWidget)

    def create_floor_group_box(self, floor_name, rooms):
        # Create a group box for a single floor
        group_box = QGroupBox(floor_name)
        vbox_layout = QVBoxLayout()
        
        # Add a checkbox for each room in the floor
        for room_name in rooms:
            checkbox = QCheckBox(room_name)
            vbox_layout.addWidget(checkbox)


        group_box.setLayout(vbox_layout)
        return group_box

# Run the application
app = QApplication(sys.argv)
window = BuildingControlApp()
window.show()
sys.exit(app.exec())

# NEEDS IMPROVEMENT 

# import sys
# from PyQt6.QtWidgets import QMainWindow, QGroupBox, QVBoxLayout, QCheckBox, QLabel, QWidget, QHBoxLayout, QPushButton, QApplication

# class BuildingControlApp(QMainWindow):
#     def __init__(self, callback=None):
#         super().__init__()
#         self.setWindowTitle("Building Controls")
#         self.setGeometry(100, 100, 640, 480)

#         # Define the layout for the central widget
#         main_layout = QHBoxLayout()

#         # Create group boxes for each floor
#         floors = {
#             "Floor 1": ["Room 1A", "Room 1B", "Room 1C", "Con. Room", "Washroom"],
#             "Floor 2": ["Room 2A", "Room 2B", "Room 2C", "Con. Room", "Washroom"],
#             "Floor 3": ["Room 3A", "Room 3B", "Room 3C", "Con. Room", "Washroom"],
#             "Floor 4": ["Room 4A", "Room 4B", "Room 4C", "Con. Room", "Washroom"]
#         }

#         # Create the GUI components for each floor
#         for floor_name, rooms in floors.items():
#             floor_group_box = self.create_floor_group_box(floor_name, rooms)
#             main_layout.addWidget(floor_group_box)

#         # Back button
#         self.back_button = QPushButton("Back", self)
#         if callback:  # Check if callback is provided
#             self.back_button.clicked.connect(callback)
#         main_layout.addWidget(self.back_button)
#    # More controls button
# self.more_button = QPushButton("More Controls",self)
# if callback: #checking if callback is provided
#    self.more_button.clicked.connect(callback)
# main_layout.insertWidget(0, self.more_button) # Add the button at the top of the layout

# # Create the GUI components for each floor
# for floor_name, rooms in floors.items():
#    floor_group_box = self.create_floor_group_box(floor_name, rooms)
#    main_layout.addWidget(floor_group_box)

            

#         # Set central widget
#         centralWidget = QWidget()
#         centralWidget.setLayout(main_layout)
#         self.setCentralWidget(centralWidget)

#     def create_floor_group_box(self, floor_name, rooms):
#         # Create a group box for a single floor
#         group_box = QGroupBox(floor_name)
#         vbox_layout = QVBoxLayout()

#         # Add a checkbox for each room in the floor
#         for room_name in rooms:
#             checkbox = QCheckBox(room_name)
#             vbox_layout.addWidget(checkbox)

#         group_box.setLayout(vbox_layout)
#         return group_box

# # Run the application
# app = QApplication(sys.argv)
# window = BuildingControlApp()  # No callback provided
# window.show()
# sys.exit(app.exec())
