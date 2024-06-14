"""
Cli tools functions
"""

import os


def clear_terminal() -> None:
    """
    Clears the terminal.
    :return: None
    """
    os.system('clear' if os.name == 'posix' else 'cls')
