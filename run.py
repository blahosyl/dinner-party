# for the `clear()` function
from os import system, name

# import sleep to show output for some time period
# package suggested by my mentor
from time import sleep

# colored terminal output
# package suggested by my mentor
from colorama import Fore, Back, Style

# import this module for classes custom written for this project
import planner

print(Fore.CYAN +
      r"""
     ____________
    <____________>
    |            |
    |            |
    |            |
     \          /
      \________/
          ||
          ||
          ||
          ||
       ___||___
      /   ||   \
      \________/
    """
      )
print(Style.RESET_ALL)

# Based on the Love Sandwiches project

# import entire library
import gspread
# import 1 class from a library
from google.oauth2.service_account import Credentials

# constant specifying what the Robot user has access to
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('ingredients')

recipes = SHEET.worksheet('main')

# get a whole worksheet as a list of lists
_data = recipes.get_all_values()
# end of code based on the Love Sandwiches project
# TESTING: print for testing/development purposes
# print(data)

# row 0 is the type of dish: starter, main, dessert or drink
# row 1 of `data` is the list of dishes
# item 0 of each row is the ingredient
# subsequent items of each row are the quantity of ingredients needed for the corresponding dish
# when an ingredient is not needed for a dish, the corresponding cell is empty

# global variables
# the row containing the names of dishes
# the [:] at the end copies the list, so that `dishes` can be changed without `data[1]` also changing
DISHES_ROW = _data[1][:]
# create a list object with `dishes_row` as the input
_dishes = planner.DishList(DISHES_ROW)

# create empty shopping list object (will be a list of lists eventually)
_shopping_list = planner.ShoppingList([])

# sets whether the planning cycle runs or not
_planning = False


# provided by my mentor Rory Patrick Sheridan (modified to fit `from...import`)
def clear():
    """
    Clear the terminal
    """
    # use `cls` for windows, `clear` for other OSes (name: `postfix`)
    system("cls" if name == "nt" else "clear")


def welcome():
    # get global variable
    global _planning
    # ask user if they want to start planning, make input uppercase
    start = input('Would you like to plan a dinner party? (Y/N): ').upper()
    # validating the input
    # while the input is not one of the allowed options
    while not start == "Y" and not start == "N":
        # ask for input again, make input uppercase
        start = input(Fore.RED + "I did not understand. Please type Y or N ").upper()
        # reset terminal color
        print(Style.RESET_ALL)
    if start == 'Y':
        print(Back.GREEN + "Let's get planning!")
        # reset terminal color
        print(Style.RESET_ALL)
        # sleep for 1.5 seconds after printing output
        sleep(1.5)
        # clear the console
        clear()
        print("Here is the list of dishes you can choose from.")
        # sleep for 2 seconds after printing output
        sleep(2)
        #  start the addition cycle
        _planning = True

    elif start == 'N':
        #  exit the program with a message
        _planning = False
        print("Maybe some other time then. Bye for now!")


def ask_more():
    """Ask the user if they want to add more dishes if there are dishes left on the list"""
    # get global variables
    global _dishes
    global _planning
    # check if there are dishes left (note: dishes[0] = '', so this should not be counted)
    if len(_dishes.dish_data) > 1:
        # ask user if they want to add a dish to the shopping list, make input uppercase
        add_dish = input('Would you like to add another dish? (Y/N): ').upper()
        # validating the input
        # while the input is not one of the allowed options
        while not add_dish == "Y" and not add_dish == "N":
            # ask for input again, make input uppercase
            add_dish = input(Fore.RED + "I did not understand. Please type Y or N ").upper()
            # reset terminal color
            print(Style.RESET_ALL)
        if add_dish == 'Y':
            # planning remains True, keeps the loop running
            clear()
            # print an empty line to visually separate the list
            print('\n')
            print("Cool, here is the list of dishes again:")
        elif add_dish == 'N':
            _planning = False
            # print an empty line to visually separate the list
            print('\n')
            print("Got it! Here is your shopping list:")
            _shopping_list.print_formatted(_shopping_list.list_data)
            print("Have fun!")
    else:
        # stop the loop
        _planning = False
        print("You have selected all the dishes. Here is your shopping list:")
        _shopping_list.print_formatted(_shopping_list.list_data)
        print("Have fun!")


welcome()

while _planning:
    _shopping_list.add_ingredients(_dishes.select_dish(), _data)
    ask_more()
