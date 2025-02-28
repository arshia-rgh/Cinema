import uuid
from datetime import datetime
from enum import Enum
from getpass import getpass

from service.auth import auth_service
from utils.cli import clear_terminal

USER = None
CUSTOMER = None
IS_LOGIN = False


class AuthenticationMenuOption(Enum):
    REGISTER = 1
    LOGIN = 2
    EXIT = 3


def authentication_menu():
    print("Please select an option:")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    option = int(input('Enter your option number: '))
    return option


def create_user_menu():
    print("Welcome to Register Menu:")
    username = uuid.uuid4().hex
    email = input("Email:\n")
    clear_terminal()
    password = getpass("Password: ( min length 8 and use at least 2 characters from [$, &, #, @] )\n")
    clear_terminal()
    phone = input("Phone: (optional)\n")
    clear_terminal()
    phone = phone if phone != '' else None
    birthdate = input("Birthdate: (example format: 1998-06-05)\n")
    registration_date = datetime.now()
    user = auth_service.register(
        username=username,
        email=email,
        password=password,
        phone=phone
    )
    auth_service.create_customer(
        user=user,
        birth_date=datetime.strptime(birthdate, "%Y-%m-%d"),
        registration_date=registration_date
    )
    print('Registered successfully.')


def login_user_menu():
    email = input("Email:\n")
    clear_terminal()
    password = getpass("Password:\n")
    clear_terminal()
    confirm_password = getpass("Confirm Password:\n")
    if password != confirm_password:
        print("Passwords do not match.")
    else:
        if auth_service.login_with_email(email, password):
            global USER, CUSTOMER, IS_LOGIN
            USER, CUSTOMER = auth_service.get_current_user_customer(email)
            IS_LOGIN = True
            print('Login successful.')


def dashboard():
    pass


if __name__ == '__main__':
    while True:
        clear_terminal()
        print('Welcome to CinemaTicket CRM 🤩')
        selected = authentication_menu()
        if selected == AuthenticationMenuOption.REGISTER.value:
            clear_terminal()
            create_user_menu()
            continue
        elif selected == AuthenticationMenuOption.LOGIN.value:
            clear_terminal()
            login_user_menu()
            if IS_LOGIN:
                dashboard()
        else:
            clear_terminal()
            print('Goodbye 👋')
            break
