# import entire library
import itertools

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
print(data)

# row 0 is the type of dish: starter, main, dessert or drink
# row 1 of `data` is the list of dishes
# item 0 of each row is the ingredient
# subsequent items of each row are the quantity of ingredients needed for the corresponding dish
# when an ingredient is not needed for a dish, the corresponding cell is empty

# ask user if they want to plan a dinner party TODO

# create empty shopping list (will be a list of lists)
shopping_list = []

# mock add ingredients to test for duplicates TODO REMOVE LATER
shopping_list.append(['flour (g)', 60.25])
shopping_list.append(['butter (g)', 100.0])


# the [:] at the end copies the list, so that `dishes` can be changed without `data[1]` also changing
dishes = data[1][:]

def print_list(list):
    """ Print available dishes """
    for i in range(1, len(list)):
        print(i,list[i])

def select_dish():
    # print the list of dishes in a numbered list
    print_list(dishes)

    # ask user to select a dish number
    dish_number = input("Select the number of the dish you'd like to add: ")

    # get the dish with the selected number from the `dishes` list
    selected_dish = dishes[int(dish_number)]

    # print the selected dish's name
    print(f'You have selected: {selected_dish}')

    # remove the selected dish from the list of available dishes
    dishes.remove(selected_dish)

    return selected_dish

def get_ingredients(selection):
    """Get list of ingredients for a selected dish, add them to `shopping_list`, return a list of lists"""
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
    return shopping_list

def add_ingredients():
    """Check `shopping_list` for pairs of items (lists) where the ingredient is the same.
    Add quantities of the ingredient together.
    Return modified `shopping_list`."""
    # this needs to be run every time items are added to `shopping_list`
    shopping_list = get_ingredients(select_dish())
    #get all pairs of items within `shopping_list`
    for x,y in itertools.combinations(shopping_list, 2):
        # if the ingredient name and unit (first item of both lists) is the same
        if x[0] == y[0]:
            # print for testing/development
            print(x, y)
            # add a new item (list) with this ingredient name and unit as its first item,
            # and the sum of the two quantities as the second item
            shopping_list.append([x[0], x[1]+y[1]])
            # remove the two original items from `shopping_list`
            shopping_list.remove(x)
            shopping_list.remove(y)
    print('Shopping list updated')
    return shopping_list

add_ingredients()


# ask user if they want to add a dish to the shopping list, make input uppercase
add_dish = input('Would you like to add another dish?(Y/N) ').upper()
# validating the input
# while the input is not one of the allowed options
while not add_dish == "Y" and not add_dish == "N":
    # ask for input again, make input uppercase
    add_dish = input("I did not understand. Please type Y or N ").upper()
if add_dish == 'Y':
    print_list(dishes)
    # create new variable called `planning`, and the whole loop should be running while it's True
elif add_dish == 'N':
    # set `planning` to False
    print_list(shopping_list)



