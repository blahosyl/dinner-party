# STANDARD PACKAGES

# import sleep to show output for some time period
# package suggested by my mentor
from time import sleep

# 3RD PARTY LIBRARIES

# colored terminal output
# package suggested by my mentor
from colorama import Fore, Back, Style

# text with ASCII art
import pyfiglet

# SELF-WRITTEN MODULES & FUNCTIONS

# general-purpose functions
from utilities import validate_y_n, clear

# code for retrieving data from the database in Google Sheets
import gsheet

# custom classes, methods & library
import planner
from pantry import check_pantry

# GET DATA FROM GOOGLE SHEETS

# get a whole worksheet as a list of lists from Google Sheets
_data = gsheet.recipes.get_all_values()
# end of code based on the Love Sandwiches project
# TESTING: print for testing/development purposes
# print(data)

# row 0 is the type of dish: starter, main, dessert or drink
# (row 0 is not used for the MVP, included here for
# scalability purposes)
# row 1 of `_data` is the list of dishes
# item 0 of each row is the ingredient
# subsequent items of each row are the quantity of ingredients
# needed for the corresponding dish
# when an ingredient is not needed for a dish, the corresponding cell is empty

# CONSTANTS

# get the row containing the names of dishes
# the [:] at the end copies the list, so that `DISHES_ROW` can be changed
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

# content and styling of message to check pantry
CHECK_PANTRY = [Back.MAGENTA
               + '\nWould you like to check your pantry '
                 'for ingredients you already have? (Y/N):'
               + Back.RESET + ' ']

# content and styling of goodbye message
GOODBYE_MESSAGE = '\n' + Fore.MAGENTA \
                  + pyfiglet.figlet_format('Have fun!', font='doom') \
                  + Fore.RESET

# instruction displayed at the end of running
START_INSTRUCTION = '\nPress RUN PROGRAM to start again'

#  GLOBAL VARIABLES

# create a DishList object with `DISHES_ROW` as the input
_dishes = planner.DishList(DISHES_ROW)

# create empty ShoppingList object (will be a list of lists eventually)
_shopping_list = planner.ShoppingList([])

# set whether the planning cycle runs or not
_planning = False


# FUNCTIONS


def welcome_text():
    """Initial screen text"""
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


def welcome():
    """
    Starts planning or ends the program
    depending on user input
    """
    # get global variable
    global _planning

    # print welcome text
    welcome_text()

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
    planner.print_formatted(_shopping_list.list_data)
    # sleep for 1.5 seconds after printing output
    sleep(1.5)
    print(GOODBYE_MESSAGE)
    print(START_INSTRUCTION)

def end_planning():
    # stop the planning loop
    global _planning
    _planning = False
    # ask if the user wants to check their pantry
    pantry = validate_y_n(CHECK_PANTRY)
    if pantry == 'Y':
        _shopping_list.check_pantry()
    # print the shopping list
    print_shopping_list_block()


def ask_more():
    """
    If there are dishes left on the list,
    ask the user if they want to add more dishes
    """
    # get global variables
    global _dishes
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
            print("\nGot it! That's enough cooking for now 🍲\n")
            end_planning()
    else:
        print('\nYou have selected all the dishes.')
        print('🌯 🍛️ 🍷 🍻 🌮 🥃 🥗 🧆 🍰 🫔 🍹 ')
        end_planning()


# RUN APP

welcome()

while _planning:
    _shopping_list.unify_ingredients(_dishes.select_dish(), _data)
    ask_more()
