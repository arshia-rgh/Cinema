# this code is based on -> https://docs.python.org/3.3/tutorial/errors.html#user-defined-exceptions

class CinemaTicketError(Exception):
    """Base class for exceptions in this module."""

    def __init__(self, message):
        self.message = message


class LongUserNameError(CinemaTicketError):
    """raised when username is more than 100 characters

    Attributes:
        value -- input value in which the error occurred
        message -- explanation of the error
    """


class InvalidUserNameError(CinemaTicketError):
    """raised when username is invalid(lowercase, uppercase letters and numbers)"""


class DuplicatedEmailError(CinemaTicketError):
    """raised when email is not unique"""


class InvalidEmailError(CinemaTicketError):
    """raised when email's formal is not correct"""


class InvalidPhoneError(CinemaTicketError):
    """raised when user's phone number is not valid"""


class ShortPasswordError(CinemaTicketError):
    """raised when password is less than 8 characters"""


class WeakPasswordError(CinemaTicketError):
    """raised when user's password doesn't have at least 2 characters
        of [$, #, &, @]
    """


class InvalidPasswordError(CinemaTicketError):
    """raised when user's password is not valid
        It should only contains lowercase, uppercase letters,
        numbers and [$, #, &, @]
    """


class LowAccountBalanceError(CinemaTicketError):
    """raised when user's bank account's balance is low"""


class InvalidRateValueError(CinemaTicketError):
    """
        raised when rate value is not between 0 and 5
    """


class UserHasConstraintError(CinemaTicketError):
    """
    raised when user has customer or manager in one to one relationship error
    """


class CustomerUpdateError(CinemaTicketError):
    """
    raised when customer update is invalid
    """


class CustomerNotFoundError(CinemaTicketError):
    """
    raised when customer does not exist
    """
