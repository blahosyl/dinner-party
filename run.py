# Use of gspread based on the Love Sandwiches project
# import entire library
import gspread
# import 1 class from a library
from google.oauth2.service_account import Credentials

# end of code based on the Love Sandwiches project

# for the `clear()` function
from os import system, name

# import sleep to show output for some time period
# package suggested by my mentor
from time import sleep

# colored terminal output
# package suggested by my mentor
from colorama import Fore, Back, Style

# text with ASCII art
import pyfiglet

# import this module for classes custom written for this project
import planner

# initial screen text
# name of the app in ASCII art using `pyfiglet`
print(Style.BRIGHT + Fore.MAGENTA +
      pyfiglet.figlet_format("Dinner Party!", font="doom")
      )
print("Designed and coded by Sylvia Blaho (github.com/blahosyl)\n" + Fore.RESET)
print("\nDo you love hosting dinner parties?  🍝 🥂 🎂 🥳"
      "\nThis app helps you plan them!"
      "\nJust select the dishes or drinks you want to make for your guests,"
      "\nand the app generates a shopping list for you!\n")

# Based on the Love Sandwiches project
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
START_INSTRUCTION = "\nPress RUN PROGRAM to start again"

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
    # ask user if they want to start planning
    start = input(Back.MAGENTA
                  + 'Would you like to plan a dinner party? (Y/N):'
                  + Back.RESET
                  + " ")
    # validating the input
    # while the input is not one of the allowed options
    while start not in {"Y", "N", "y", "n"}:
        # ask for input again
        start = input(Back.RED
                      + f'You typed "' + Fore.CYAN + start + Fore.RESET
                      + f'" – I don\'t understand that 🤔 Please type Y or N:'
                      + Back.RESET + " ")
    if start == 'Y' or start == 'y':
        print("\nLet's get planning! 🍾\n")
        # sleep for 1.5 seconds after printing output
        sleep(1.5)
        # clear the console
        clear()
        print("\nHere is the list of dishes you can choose from 🤓")
        #  start the addition cycle
        _planning = True

    elif start == 'N' or start == 'n':
        #  exit the program with a message
        _planning = False
        # clear the terminal
        print("\nMaybe some other time, then 👋\n")
        # sleep for 1.5 seconds after printing output
        sleep(1.5)
        # clear the console
        clear()
        print(Fore.MAGENTA +
              pyfiglet.figlet_format("Bye for now!", font="doom")
              + Fore.RESET)
        print(START_INSTRUCTION)


def print_shopping_list_block():
    """
    Prints confirmation of planning ending,
    the shopping list, the goodbye message
    and start instruction
    """
    goodbye_message = "\n" + Fore.MAGENTA \
                      + pyfiglet.figlet_format("Have fun!", font="doom") \
                      + Fore.RESET
    print("\nHere comes your shopping list 📋")
    # sleep for 1.5 seconds after printing output
    sleep(1.5)
    # clear the screen
    clear()
    print(Fore.GREEN + "\nSHOPPING LIST" + Fore.RESET)
    _shopping_list.print_formatted(_shopping_list.list_data)
    # sleep for 1.5 seconds after printing output
    sleep(1.5)
    print(goodbye_message)
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
        add_dish = input(Back.MAGENTA
                         + 'Would you like to add another dish? (Y/N):'
                         + Back.RESET + " ")
        # validating the input
        # while the input is not one of the allowed options
        while add_dish not in {"Y", "N", "y", "n"}:
            # ask for input again
            add_dish = input(Back.RED
                      + f'You typed "' + Fore.CYAN + add_dish + Fore.RESET
                      + f'" – I don\'t understand that 🤔 Please type Y or N:'
                      + Back.RESET + " ")
        if add_dish == 'Y' or add_dish == 'y':
            # planning remains True, keeps the loop running
            clear()
            print("\nCool, here is the list of dishes again 🤓")
        elif add_dish == 'N' or add_dish == 'n':
            _planning = False
            print("\nGot it! That's enough cooking for now 🍲\n")
            print_shopping_list_block()
    else:
        # stop the loop
        _planning = False
        print("\nYou have selected all the dishes.")
        print("🌯 🍛️ 🍷 🍻 🌮 🥃 🥗 🧆 🍰 🫔 🍹 ")
        print_shopping_list_block()


welcome()

while _planning:
    _shopping_list.unify_ingredients(_dishes.select_dish(), _data)
    ask_more()