# import sleep to show output for some time period
# package suggested by my mentor
from time import sleep

# Use of gspread based on the Love Sandwiches project
# import entire library
import gspread
# import 1 class from a library
from google.oauth2.service_account import Credentials
# end of code based on the Love Sandwiches project

# colored terminal output
# package suggested by my mentor
from colorama import Fore, Back, Style

# text with ASCII art
import pyfiglet

# self-written general-purpose functions
from utilities import validate_y_n, clear

# self-written custom classes, methods & library
import planner

# initial screen text
# name of the app in ASCII art using `pyfiglet`
print(Style.BRIGHT + Fore.MAGENTA +
      pyfiglet.figlet_format('Dinner Party!', font='doom')
      )
print('Designed and coded by Sylvia Blaho (github.com/blahosyl)\n'
      + Fore.RESET)
print('\nDo you love hosting dinner parties?  🍝 🥂 🎂 🥳'
      '\nThis app helps you plan them!'
      '\nJust select the dishes or drinks you want to make for your guests,'
      '\nand the app generates a shopping list for you!\n')

# Based on the Love Sandwiches project
# constant specifying what the Robot user has access to
SCOPE = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive'
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('ingredients')
START_INSTRUCTION = '\nPress RUN PROGRAM to start again'

recipes = SHEET.worksheet('main')

# get a whole worksheet as a list of lists
_data = recipes.get_all_values()
# end of code based on the Love Sandwiches project
# TESTING: print for testing/development purposes
# print(data)

# row 0 is the type of dish: starter, main, dessert or drink
# row 1 of `data` is the list of dishes
# item 0 of each row is the ingredient
# subsequent items of each row are the quantity of ingredients
# needed for the corresponding dish
# when an ingredient is not needed for a dish, the corresponding cell is empty

# global variables
# the row containing the names of dishes
# the [:] at the end copies the list, so that `dishes` can be changed
# without `data[1]` also changing
DISHES_ROW = _data[1][:]

# content and styling of initial question to start planning
INITIAL_QUESTION = [Back.MAGENTA
                    + 'Would you like to plan a dinner party? (Y/N):'
                    + Back.RESET
                    + ' ']
# content and styling of message asking to add more dishes
MORE_DISHES = [Back.MAGENTA
               + 'Would you like to add another dish? (Y/N):'
               + Back.RESET + ' ']

# content and styling of goodbye message
GOODBYE_MESSAGE = '\n' + Fore.MAGENTA \
                  + pyfiglet.figlet_format('Have fun!', font='doom') \
                  + Fore.RESET

# create a list object with `dishes_row` as the input
_dishes = planner.DishList(DISHES_ROW)

# create empty shopping list object (will be a list of lists eventually)
_shopping_list = planner.ShoppingList([])

# sets whether the planning cycle runs or not
_planning = False


def welcome():
    """
    Starts planning or ends the program
    depending on user input
    """
    # get global variable
    global _planning
    # ask if user wants to start planning
    start = validate_y_n(INITIAL_QUESTION)

    if start == 'Y':
        print("\nLet's get planning! 🍾\n")
        # sleep for 1.5 seconds after printing output
        sleep(1.5)
        # clear the console
        clear()
        print('\nHere is the list of dishes you can choose from 🤓')
        #  start the addition cycle
        _planning = True

    elif start == 'N':
        #  exit the program with a message
        _planning = False
        # clear the terminal
        print('\nMaybe some other time, then 👋\n')
        # sleep for 1.5 seconds after printing output
        sleep(1.5)
        # clear the console
        clear()
        print(GOODBYE_MESSAGE)
        print(START_INSTRUCTION)


def print_shopping_list_block():
    """
    Prints confirmation of planning ending,
    the shopping list, the goodbye message
    and start instruction
    """
    print('\nHere comes your shopping list 📋')
    # sleep for 1.5 seconds after printing output
    sleep(1.5)
    # clear the screen
    clear()
    print(Fore.GREEN + '\nSHOPPING LIST' + Fore.RESET)
    _shopping_list.print_formatted(_shopping_list.list_data)
    # sleep for 1.5 seconds after printing output
    sleep(1.5)
    print(GOODBYE_MESSAGE)
    print(START_INSTRUCTION)


def ask_more():
    """
    If there are dishes left on the list,
    ask the user if they want to add more dishes
    """
    # get global variables
    global _dishes
    global _planning
    # check if there are dishes left
    # (note: dishes[0] = '', so this should not be counted)
    if len(_dishes.dish_data) > 1:
        # ask user if they want to add a dish to the shopping list,
        add_dish = validate_y_n(MORE_DISHES)
        if add_dish == 'Y':
            # planning remains True, keeps the loop running
            clear()
            print('\nCool, here is the list of dishes again 🤓')
        elif add_dish == 'N':
            _planning = False
            print("\nGot it! That's enough cooking for now 🍲\n")
            print_shopping_list_block()
    else:
        # stop the loop
        _planning = False
        print('\nYou have selected all the dishes.')
        print('🌯 🍛️ 🍷 🍻 🌮 🥃 🥗 🧆 🍰 🫔 🍹 ')
        print_shopping_list_block()


welcome()

while _planning:
    _shopping_list.unify_ingredients(_dishes.select_dish(), _data)
    ask_more()
