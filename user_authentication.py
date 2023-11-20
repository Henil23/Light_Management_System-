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

    def register_user(self, first_name, last_name, email, password):
        hashed_password = self.hash_password(password)

        user_data = {
            'id': len(self.users) + 1,
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': hashed_password
        }

        self.users.append(user_data)
        self.save_users()
        print("User registered successfully.")

    def authenticate_user(self,email, password):
        hashed_password = self.hash_password(password)

        for user in self.users:
            if user['email'] == email and user['password'] == hashed_password:
                print("Login successful. Welcome, {}!".format(user['first_name']))
                return True

        print("Incorrect username or password. Please try again.")
        return False

    def forgot_password(self):
        print("If you forgot your password, please contact the management for assistance.")

    def log_out(self):
        print("You are logged out.")

