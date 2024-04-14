# for the `clear()` function
from os import system, name

# import sleep to show output for some time period
from time import sleep

# import custom class
import planner

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
data = recipes.get_all_values()
# end of code based on the Love Sandwiches project
# TESTING: print for testing/development purposes
# print(data)

# row 0 is the type of dish: starter, main, dessert or drink
# row 1 of `data` is the list of dishes
# item 0 of each row is the ingredient
# subsequent items of each row are the quantity of ingredients needed for the corresponding dish
# when an ingredient is not needed for a dish, the corresponding cell is empty


# the [:] at the end copies the list, so that `dishes` can be changed without `data[1]` also changing
dishes_row = data[1][:]
# create a list object with `dishes_row` as the input
dishes = planner.DishList(dishes_row)

# create empty shopping list object (will be a list of lists eventually)
shopping_list = planner.ShoppingList([])

# sets whether the planning cycle runs or not
planning = False


# provided by my mentor Rory Patrick Sheridan (modified to fit `from...import`)
def clear():
    """
    Clear the terminal
    """
    # use `cls` for windows, `clear` for other OSes (name: `postfix`)
    system("cls" if name == "nt" else "clear")


def welcome():
    # get global variable
    global planning
    # ask user if they want to start planning, make input uppercase
    start = input('Would you like to plan a dinner party? (Y/N): ').upper()
    # validating the input
    # while the input is not one of the allowed options
    while not start == "Y" and not start == "N":
        # ask for input again, make input uppercase
        start = input("I did not understand. Please type Y or N ").upper()
    if start == 'Y':
        print("Let's get planning!")
        # sleep for 1.5 seconds after printing output
        sleep(1.5)
        # clear the console
        clear()
        print("Here is the list of dishes you can choose from.")
        # sleep for 2 seconds after printing output
        sleep(2)
        #  start the addition cycle
        planning = True

    elif start == 'N':
        #  exit the program with a message
        planning = False
        print("Maybe some other time then. Bye for now!")


def ask_more():
    """Ask the user if they want to add more dishes if there are dishes left on the list"""
    # get global variables
    global dishes
    global planning
    # check if there are dishes left (note: dishes[0] = '', so this should not be counted)
    if len(dishes.dish_data) > 1:
        # ask user if they want to add a dish to the shopping list, make input uppercase
        add_dish = input('Would you like to add another dish? (Y/N): ').upper()
        # validating the input
        # while the input is not one of the allowed options
        while not add_dish == "Y" and not add_dish == "N":
            # ask for input again, make input uppercase
            add_dish = input("I did not understand. Please type Y or N ").upper()
        if add_dish == 'Y':
            # planning remains True, keeps the loop running
            clear()
            # print an empty line to visually separate the list
            print('\n')
            print("Cool, here is the list of dishes again:")
        elif add_dish == 'N':
            planning = False
            # print an empty line to visually separate the list
            print('\n')
            print("Got it! Here is your shopping list:")
            shopping_list.print_string()
            print("Have fun!")
    else:
        # stop the loop
        planning = False
        print("You have selected all the dishes. Here is your shopping list:")
        shopping_list.print_string()
        print("Have fun!")


welcome()

while planning:
    shopping_list.add_ingredients(dishes.select_dish(), data)
    ask_more()
