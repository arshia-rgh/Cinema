# this code is based on -> https://docs.python.org/3.3/tutorial/errors.html#user-defined-exceptions

class CinemaTicketError(Exception):
    """Base class for exceptions in this module."""
    pass


class LongUserNameError(CinemaTicketError):
    """raised when username is more than 100 characters

    Attributes:
        value -- input value in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, value, message):
        self.value = value
        self.message = message


class InvalidUserNameError(CinemaTicketError):
    """raised when username is invalid(lowercase, uppercase letters and numbers)"""

    def __init__(self, value, message):
        self.value = value
        self.message = message


class DuplicatedEmailError(CinemaTicketError):
    """raised when email is not unique"""

    def __init__(self, value, message):
        self.value = value
        self.message = message


class InvalidEmailError(CinemaTicketError):
    """raised when email's formal is not correct"""

    def __init__(self, value, message):
        self.value = value
        self.message = message


class InvalidPhoneError(CinemaTicketError):
    """raised when user's phone number is not valid"""

    def __init__(self, value, message):
        self.value = value
        self.message = message


class ShortPasswordError(CinemaTicketError):
    """raised when password is less than 8 characters"""

    def __init__(self, value, message):
        self.value = value
        self.message = message


class WeakPasswordError(CinemaTicketError):
    """raised when user's password doesn't have at least 2 characters
        of [$, #, &, @]
    """

    def __init__(self, value, message):
        self.value = value
        self.message = message


class InvalidPasswordError(CinemaTicketError):
    """raised when user's password is not valid
        It should only contains lowercase, uppercase letters,
        numbers and [$, #, &, @]
    """

    def __init__(self, value, message):
        self.value = value
        self.message = message


class LowAccountBalanceError(CinemaTicketError):
    """raised when user's bank account's balance is low"""

    def __init__(self, value, message):
        self.value = value
        self.message = message

class InvalidRateValueError(CinemaTicketError):
    """
        raised when rate value is not between 0 and 5
    """
    def __init__(self, value, message):
        self.value = value
        self.message = message 