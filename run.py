# get combinations from a list
import itertools

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


# provided by my mentor Rory Patrick Sheridan (modified to fit `from...import`)
def clear():
    """
    Clear the terminal
    """
    # use `cls` for windows, `clear` for other OSes (name: `postfix`)
    system("cls" if name == "nt" else "clear")


# TODO put this block in a function
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


# create empty shopping list (will be a list of lists)
shopping_list = []

# the [:] at the end copies the list, so that `dishes` can be changed without `data[1]` also changing
dishes_row = data[1][:]
dishes = planner.DishList(dishes_row)


def print_shopping_list():
    """ Print shopping list """
    # print an empty line to visually separate the list
    print('\n')
    for i in range(0, len(shopping_list)):
        # print(shopping_list[i][0], shopping_list[i][1])
        print_string = shopping_list[i][0]
        opening = print_string.index('(')
        print_string = print_string[:opening-1] + ': ' + str(shopping_list[i][1]) + print_string[opening-1:]
        print_string = print_string.replace('(', '')
        print_string = print_string.replace(')', '')
        print(print_string)
    # print an empty line to visually separate the list
    print('\n')
    

def get_ingredients(selection):
    """Get list of ingredients for a selected dish, add them to `shopping_list`, return a list of lists"""
    # print an empty line to visually separate the block
    print('\n')
    print(f'Ingredients for {selection}')
    # get the index of the selected dish in the database
    selection_index = data[1].index(selection)
    # go through each row
    for row in data:
        # if the cell in the row under the selected dish has content (ingredient quantity)
        # and it's not one of the first 2 rows
        if row[selection_index] and data.index(row) > 1:
            # print the ingredient name and quantity
            print(row[0]+' '+row[selection_index])
            # add the list [ingredient, quantity(converted to a float)] to the shopping list
            shopping_list.append([row[0], float(row[selection_index])])
    # print an empty line to visually separate the block
    print('\n')
    return shopping_list


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
            print_shopping_list()
            print("Have fun!")
    else:
        # stop the loop
        planning = False
        print("You have selected all the dishes. Here is your shopping list:")
        print_shopping_list()
        print("Have fun!")


def add_ingredients():
    """Check `shopping_list` for pairs of items (lists) where the ingredient is the same.
    Add quantities of the ingredient together.
    Return modified `shopping_list`."""
    # this needs to be run every time items are added to `shopping_list`
    shopping_list = get_ingredients(dishes.select_dish())
    # get all pairs of items within `shopping_list`
    for x, y in itertools.combinations(shopping_list, 2):
        # if the ingredient name and unit (first item of both lists) is the same
        if x[0] == y[0]:
            # TESTING: print for testing/development
            print(x, y)
            # add a new item (list) with this ingredient name and unit as its first item,
            # and the sum of the two quantities as the second item
            shopping_list.append([x[0], x[1]+y[1]])
            # remove the two original items from `shopping_list`
            shopping_list.remove(x)
            shopping_list.remove(y)
    print('Shopping list updated\n')
    ask_more()
    return shopping_list


while planning:
    add_ingredients()
