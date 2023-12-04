# Developers:

#################################
# Henil Patel                   #
# Muhammad Asim                 # 
# Amandeep Kaur                 #
# Sadiya Islam                  #
# Nischey                       #
#################################

# importing necessary libraries and python files 
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox, QFormLayout, QDialog, QStackedWidget, QCheckBox
from PyQt6.QtCore import pyqtSignal, Qt
import userauth
from test_homepage import Ui_MainWindow
import re

# This function is used to set up the user interface of the application. It's usually called after the UI has been set up.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login System")  #setting the window title
        self.setGeometry(100, 100, 10000, 10000) # setting the coordinates to set the window size
        # Create a stacked widget to manage multiple pages (widgets)
        self.stacked_widget = QStackedWidget()  
        self.setCentralWidget(self.stacked_widget)
        # Create instances of the login, register, and password recovery widgets
        self.login_widget = LoginWidget(self)
        self.register_widget = RegisterWidget(self)
        self.password_recovery_widget = PasswordRecoveryWidget(self)
        self.stacked_widget.addWidget(self.login_widget)
        self.stacked_widget.addWidget(self.register_widget)
        self.stacked_widget.addWidget(self.password_recovery_widget)

         # Connect signals to corresponding slots for navigation
        self.login_widget.sign_up_clicked.connect(self.switch_to_register)
        self.login_widget.forgot_password_clicked.connect(self.switch_to_password_recovery)
        self.register_widget.registration_successful.connect(self.switch_to_login)
        self.register_widget.login_instead_clicked.connect(self.switch_to_login)
        self.password_recovery_widget.back_to_login_clicked.connect(self.switch_to_login)
     # Methods to switch between different widgets in the stacked widget
    def switch_to_register(self):
        self.stacked_widget.setCurrentWidget(self.register_widget)

    def switch_to_password_recovery(self):
        self.stacked_widget.setCurrentWidget(self.password_recovery_widget)

    def switch_to_login(self):
        self.stacked_widget.setCurrentWidget(self.login_widget)
# Widget for login functionality
# class LoginWidget(QWidget):
#     # Custom signals to indicate user actions
#     sign_up_clicked = pyqtSignal()
#     forgot_password_clicked = pyqtSignal()

#     def __init__(self, parent):
#         super().__init__(parent)
#         self.initUI()
#     # Initialize the UI components for the login widget
#     def initUI(self):
#         layout = QFormLayout()
#         self.user_id_input = QLineEdit()
#         self.password_input = QLineEdit()
#         login_button = QPushButton("Login")
#         signup_button = QPushButton("Sign Up")
#         forgot_password_button = QPushButton("Forgot Password")
#     # Add input fields and buttons to the form layout
#         layout.addRow(QLabel("User ID"), self.user_id_input)
#         layout.addRow(QLabel("Password"), self.password_input)
#         self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
#         layout.addRow(login_button,signup_button)

#         # layout.addRow(signup_button)
#         layout.addRow(forgot_password_button)
#         self.setLayout(layout)
#     # Connect button clicks to their respective methods
#         login_button.clicked.connect(self.login)
#         signup_button.clicked.connect(self.sign_up_clicked)
#         forgot_password_button.clicked.connect(self.forgot_password_clicked)
#      # Login method to authenticate user
#     def login(self):
#         user_id = self.user_id_input.text()
#         password = self.password_input.text()
#          # Authenticate using the userauth module
#         if userauth.authenticate_user(user_id, password):
#             self.open_home_page()
#         else:
#             QMessageBox.critical(self, "Login Failed", "Invalid user ID or password.")
#     # Method to open the home page after successful login
#     def open_home_page(self):
#         self.main_window = QMainWindow()
#         self.ui = Ui_MainWindow()
#         self.ui.homepageUi(self.main_window)
#         self.main_window.show()
#         self.parent().parent().close()
class LoginWidget(QWidget):
    sign_up_clicked = pyqtSignal()
    forgot_password_clicked = pyqtSignal()
 
    def __init__(self, parent):
        super().__init__(parent)
        self.initUI()
 
    def initUI(self):
        layout = QVBoxLayout()
        form_layout = QFormLayout()
 
        self.user_id_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
 
        login_button = QPushButton("Login")
        signup_button = QPushButton("Sign Up")
        forgot_password_button = QPushButton("Forgot Password")
 
        form_layout.addRow("User ID:", self.user_id_input)
        form_layout.addRow("Password:", self.password_input)
 
        button_layout = QVBoxLayout()
        button_layout.addWidget(login_button)
        button_layout.addWidget(signup_button)
        button_layout.addWidget(forgot_password_button)
 
       
 
        layout.addLayout(form_layout)
        layout.addLayout(button_layout)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
 
        signup_button.clicked.connect(self.sign_up_clicked)
        forgot_password_button.clicked.connect(self.forgot_password_clicked)
        login_button.clicked.connect(self.login)
 
        # Set a maximum width for text input boxes
        max_width = 200
        self.user_id_input.setMaximumWidth(max_width)
        self.password_input.setMaximumWidth(max_width)
 
        self.setLayout(layout)
 
    def login(self):
        user_id = self.user_id_input.text()
        password = self.password_input.text()
        if userauth.authenticate_user(user_id, password):
            self.open_home_page()
        else:
            QMessageBox.critical(self, "Login Failed", "Invalid user ID or password.")
 
    def open_home_page(self):
        self.main_window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.homepageUi(self.main_window)
        self.main_window.show()
        self.parent().parent().close()
# Widget for registration functionality
class RegisterWidget(QWidget):
    # Custom signals for registration and switching to login
    registration_successful = pyqtSignal()
    login_instead_clicked = pyqtSignal()

    def __init__(self, parent):
        super().__init__(parent)
        self.initUI()

    # Initialize the UI components for the registration widget
    def initUI(self):
        layout = QFormLayout()
        self.name_input = QLineEdit()
        self.username_input = QLineEdit()
        self.email_input = QLineEdit()
        self.dob_input = QLineEdit()
        self.location_input = QLineEdit()
        self.phone_input = QLineEdit()
        self.password_input = QLineEdit()
        sign_up_button = QPushButton("Sign Up")
        login_instead_button = QPushButton("Log In Instead")
        self.terms_acceptance_checkbox = QCheckBox("I accept the Terms and Conditions")

        layout.addRow(QLabel("Full Name"), self.name_input)
        layout.addRow(QLabel("Username"), self.username_input)
        layout.addRow(QLabel("Email"), self.email_input)
        layout.addRow(QLabel("Date of Birth"), self.dob_input)
        layout.addRow(QLabel("Location"), self.location_input)
        layout.addRow(QLabel("Phone Number"), self.phone_input)
        layout.addRow(QLabel("Password"), self.password_input)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addRow(self.terms_acceptance_checkbox)
        layout.addRow(sign_up_button, login_instead_button)
        self.setLayout(layout)

        sign_up_button.clicked.connect(self.register)
        login_instead_button.clicked.connect(self.login_instead_clicked)  # Corrected signal name
    # function that will help user to login if they are already signed up
    def login_instead(self):
        self.login_instead_clicked.emit()
    # function that will help user to register/sign up
    def register(self):
        name = self.name_input.text()
        username = self.username_input.text()
        email = self.email_input.text()
        dob = self.dob_input.text()
        location = self.location_input.text()  # Add this line
        phone = self.phone_input.text()
        password = self.password_input.text()  # Add this line

        # Validate the format of Date of Birth (DOB)
        dob_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
        if not dob_pattern.match(dob):
            QMessageBox.critical(self, "Invalid Date of Birth", "Please enter DOB in YYYY-MM-DD format.")
            return

        # Validate the format of Phone Number
        phone_pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
        if not phone_pattern.match(phone):
            QMessageBox.critical(self, "Invalid Phone Number", "Please enter phone number in XXX-XXX-XXXX format.")
            return

        terms_accepted = self.terms_acceptance_checkbox.isChecked()

        if not terms_accepted:
            QMessageBox.critical(self, "Terms and Conditions", "Please accept the Terms and Conditions.")
            return

        user_info = {
            'name': name,
            'email': email,
            'dob': dob,
            'location': location,
            'phone': phone,
            'password': password,
        }
        # if user enters all the information correctly then this message will be displayed
        if userauth.register_user(username, user_info):
            QMessageBox.information(self, "Registration Successful", "You have registered successfully!")
            self.registration_successful.emit()
        # if they are already registered then they will see this message
        else:
            QMessageBox.critical(self, "Registration Failed", "Username already exists.")
# Class where a function is made in case if the user forgots the password.
class PasswordRecoveryWidget(QDialog):
    back_to_login_clicked = pyqtSignal()

    def __init__(self, parent):
        super().__init__(parent)
        self.initUI()
    # this will be triggered when they will press forgot button
    def initUI(self):
        layout = QVBoxLayout()
        support_label = QLabel("Please contact support using your registered email address.")
        back_to_login_button = QPushButton("Back to Login")

        layout.addWidget(support_label)
        layout.addWidget(back_to_login_button)
        self.setLayout(layout)

        back_to_login_button.clicked.connect(self.back_to_login_clicked.emit)
# function that will run the program
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

