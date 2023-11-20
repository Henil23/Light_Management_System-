


from userInput import UserInputModule
from user_authentication import UserAuthenticationModule


user_input_module = UserInputModule()
user_auth_module = UserAuthenticationModule()

def main():
    user_input_module = UserInputModule()
    user_auth_module = UserAuthenticationModule()

    while True:
        print("1. Register a user")
        print("2. Authenticate a user")
        print("3. Forgot password")
        print("4. Exit")

        choice = user_input_module.get_user_input("Enter your choice: ")

        if choice == '1':
            register_user(user_input_module, user_auth_module)
        elif choice == '2':
            authenticate_user(user_input_module, user_auth_module)
        elif choice == '3':
            forgot_password(user_auth_module)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def register_user(user_input_module, user_auth_module):
    first_name = user_input_module.get_user_input("Enter first name: ")
    last_name = user_input_module.get_user_input("Enter last name: ")
    # employee_number = user_input_module.get_user_input("Enter employee number: ")
    email = user_input_module.get_user_input("Enter email: ")
    # date_of_birth = user_input_module.get_user_input("Enter date of birth (YYYY-MM-DD): ")
    # contact = user_input_module.get_user_input("Enter contact number: ")
    # address = user_input_module.get_user_input("Enter address: ")
    #username = user_input_module.get_user_input("Enter username: ")
    password = user_input_module.get_password_input()

    user_auth_module.register_user(first_name, last_name, email,password)
##########################################################################

def authenticate_user(user_input_module, user_auth_module):
    auth_email = user_input_module.get_user_input("Enter email for authentication: ")
    auth_password = user_input_module.get_password_input()
    user_auth_module.authenticate_user(auth_email, auth_password)

def forgot_password(user_auth_module):
    user_auth_module.forgot_password()

if __name__ == "__main__":
    main()
