
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox, QFormLayout, QDialog, QStackedWidget, QCheckBox
from PyQt6.QtCore import pyqtSignal
import userauth
from test_homepage import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login System")
        self.setGeometry(100, 100, 400, 300)
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.login_widget = LoginWidget(self)
        self.register_widget = RegisterWidget(self)
        self.password_recovery_widget = PasswordRecoveryWidget(self)

        self.stacked_widget.addWidget(self.login_widget)
        self.stacked_widget.addWidget(self.register_widget)
        self.stacked_widget.addWidget(self.password_recovery_widget)

        self.login_widget.sign_up_clicked.connect(self.switch_to_register)
        self.login_widget.forgot_password_clicked.connect(self.switch_to_password_recovery)

        self.register_widget.registration_successful.connect(self.switch_to_login)
        self.register_widget.login_instead_clicked.connect(self.switch_to_login)

        self.password_recovery_widget.back_to_login_clicked.connect(self.switch_to_login)

    def switch_to_register(self):
        self.stacked_widget.setCurrentWidget(self.register_widget)

    def switch_to_password_recovery(self):
        self.stacked_widget.setCurrentWidget(self.password_recovery_widget)

    def switch_to_login(self):
        self.stacked_widget.setCurrentWidget(self.login_widget)

class LoginWidget(QWidget):
    sign_up_clicked = pyqtSignal()
    forgot_password_clicked = pyqtSignal()

    def __init__(self, parent):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QFormLayout()
        self.user_id_input = QLineEdit()
        self.password_input = QLineEdit()
        login_button = QPushButton("Login")
        signup_button = QPushButton("Sign Up")
        forgot_password_button = QPushButton("Forgot Password")

        layout.addRow(QLabel("User ID"), self.user_id_input)
        layout.addRow(QLabel("Password"), self.password_input)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addRow(login_button)

        layout.addRow(signup_button)
        layout.addRow(forgot_password_button)
        self.setLayout(layout)

        login_button.clicked.connect(self.login)
        signup_button.clicked.connect(self.sign_up_clicked)
        forgot_password_button.clicked.connect(self.forgot_password_clicked)

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

class RegisterWidget(QWidget):
    registration_successful = pyqtSignal()
    login_instead_clicked = pyqtSignal()

    def __init__(self, parent):
        super().__init__(parent)
        self.initUI()

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
        login_instead_button.clicked.connect(self.login_instead)

    def register(self):
        name = self.name_input.text()
        username = self.username_input.text()
        email = self.email_input.text()
        dob = self.dob_input.text()
        location = self.location_input.text()
        phone = self.phone_input.text()
        password = self.password_input.text()
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

        if userauth.register_user(username, user_info):
            QMessageBox.information(self, "Registration Successful", "You have registered successfully!")
            self.registration_successful.emit()
        else:
            QMessageBox.critical(self, "Registration Failed", "Username already exists.")

    def login_instead(self):
        self.login_instead_clicked.emit()

class PasswordRecoveryWidget(QDialog):
    back_to_login_clicked = pyqtSignal()

    def __init__(self, parent):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        support_label = QLabel("Please contact support using your registered email address.")
        back_to_login_button = QPushButton("Back to Login")

        layout.addWidget(support_label)
        layout.addWidget(back_to_login_button)
        self.setLayout(layout)

        back_to_login_button.clicked.connect(self.back_to_login_clicked.emit)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

