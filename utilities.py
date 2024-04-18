# a collection of general-purpose functions

# STANDARD PACKAGES

# for the `clear()` function
from os import system, name

# 3RD PARTY LIBRARIES

# colored terminal output
# package suggested by my mentor
from colorama import Fore, Back


def validate_y_n(prompt):
    """
    Get and validate user input to Y/N question
    :return: validated user input
    """
    user_input = input(prompt[0])
    # validating the input
    # while the input is not one of the allowed options
    while user_input not in {'Y', 'N', 'y', 'n'}:
        # ask for input again
        user_input = input(
                           f'{Back.RED}You typed "{Fore.CYAN}{user_input}' 
                           f'{Fore.RESET}" – I don\'t understand that 🤔'
                           f' Please type Y or N:{Back.RESET } '
                           )
    # make returned validate input uppercase
    # this should only happen at this point,
    # so that the error msg can return the original input
    return user_input.upper()


def validate_range(prompt: list, num_type, lower, upper=float('inf')):
    """
    Validate user input: number in specified range
    :param prompt: list, the content of the initial `input`
    It has to be a list, because using colorama makes it
    too complicated to be a string
    :param num_type: int or float, the type of number input accepted
    :param lower: int, lower bound of the range (incl.)
    :param upper: int, upper bound of the range (incl.)
    :return: validated input: integer in range
    """
    # customise the text of error messages
    # both for the `while` loop and `except`
    # only include "whole" in the text if only integers are accepted
    if num_type == int:
        whole = 'whole '
    else:
        whole = ''
    # change text depending on whether there is an `upper` param
    if upper == float('inf'):
        upper_text = [f'that is {lower} or above']
    else:
        upper_text = [f'between {lower} and {upper}']

    # in the following `try/except block`, using the `error` variable and
    # moving the "out of range" error logic after `break` was suggested
    # by Victor H.

    # the error message to be printed
    error = None

    while True:
        # if there is an error, print its value
        if error:
            print(error)
        try:
            user_input = input(prompt[0])
            user_input = num_type(user_input)

            # if the number is in range, proceed
            if lower <= user_input <= upper:
                break
            error = f'\n{Back.RED}Number "{Fore.CYAN}{user_input:g}'\
                    f'{Fore.RESET}" out of range 🤔 '\
                    f'Please type a number {upper_text[0]}.'\
                    f'{Back.RESET} '
        except ValueError:
            # while the input is not one of the allowed options
            # ask for input again
            error = f'\n{Back.RED}{Fore.CYAN}"{user_input}{Fore.RESET}'\
                  '" is not a valid number 🤔 '\
                  f'Please type a {whole}number {upper_text[0]}.'\
                  f'{Back.RESET}'
    return user_input


# provided by my mentor Rory Patrick Sheridan (modified to fit `from...import`)
def clear():
    """
    Clear the terminal
    """
    # use `cls` for windows, `clear` for other OSes (name: `postfix`)
    system('cls' if name == 'nt' else 'clear')
