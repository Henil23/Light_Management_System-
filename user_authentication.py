import hashlib
import json

class UserAuthenticationModule:
    def __init__(self, file_path='user_data.json'):
        self.file_path = file_path
        self.users = self.load_users()

    def load_users(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_users(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.users, file)

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, first_name, last_name, employee_number, email, date_of_birth, contact, address, username, password):
        hashed_password = self.hash_password(password)

        user_data = {
            'id': len(self.users) + 1,
            'first_name': first_name,
            'last_name': last_name,
            'employee_number': employee_number,
            'email': email,
            'date_of_birth': date_of_birth,
            'contact': contact,
            'address': address,
            'username': username,
            'password': hashed_password
        }

        self.users.append(user_data)
        self.save_users()
        print("User registered successfully.")

    def authenticate_user(self, username, password):
        hashed_password = self.hash_password(password)

        for user in self.users:
            if user['username'] == username and user['password'] == hashed_password:
                print("Login successful. Welcome, {}!".format(username))
                return True

        print("Incorrect username or password. Please try again.")
        return False

    def forgot_password(self):
        print("If you forgot your password, please contact the management for assistance.")

    def log_out(self):
        print("User logged out.")

