# user_input_module.py

class UserInputModule:
    @staticmethod
    def get_user_input(prompt):
        return input(prompt)

    @staticmethod
    def get_password_input():
        # For better security, you might want to use getpass module to hide password input
        return input("Enter password: ")

    @staticmethod
    def get_confirmation(prompt):
        response = input(prompt).lower()
        return response == 'y' or response == 'yes'