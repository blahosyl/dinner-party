# a collection of general-purpose functions

# for the `clear()` function
from os import system, name

# colored terminal output
# package suggested by my mentor
from colorama import Fore, Back


def validate_y_n(starting_question):
    """
    Get and validate user input to Y/N question
    :return: validated user input
    """
    user_input = input(starting_question[0])
    # validating the input
    # while the input is not one of the allowed options
    while user_input not in {'Y', 'N', 'y', 'n'}:
        # ask for input again
        user_input = input(Back.RED
                           + f'You typed "' + Fore.CYAN + user_input
                           + Fore.RESET
                           + f'" – I don\'t understand that 🤔'
                             f' Please type Y or N:'
                           + Back.RESET + ' ')
    return user_input


def validate_range(text: list, num_type, lower, upper=float('inf')):
    """
    Validate user input: number in specified range
    :param text: list, the content of the initial `input`
    It has to be a list, because using colorama makes it
    too complicated to be a string
    :param num_type: int or float, the type of number input accepted
    :param lower: int, lower bound of the range (incl.)
    :param upper: int, upper bound of the range (incl.)
    :return: validated input: integer in range
    """
    while True:
        try:
            # customised the text of error messages
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
            user_input = input(text[0])
            user_input = num_type(user_input)
            while user_input < lower or user_input > upper:
                user_input = num_type(
                    input(Back.RED + f'Number "' + Fore.CYAN + f'{user_input}'
                          + Fore.RESET + '" out of range 🤔 '
                          f'Please type a number {upper_text[0]}:'
                          + Back.RESET + " "))
            break
        except ValueError:
            # while the input is not one of the allowed options
            # ask for input again
            print(Back.RED + '"' + Fore.CYAN + f'{user_input}' + Fore.RESET
                  + f'" is not a valid number 🤔 '
                    f'Please type a {whole}number {upper_text[0]}.'
                  + Back.RESET)
    return user_input


# provided by my mentor Rory Patrick Sheridan (modified to fit `from...import`)
def clear():
    """
    Clear the terminal
    """
    # use `cls` for windows, `clear` for other OSes (name: `postfix`)
    system('cls' if name == 'nt' else 'clear')
