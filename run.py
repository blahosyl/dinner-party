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

# the [:] at the end copies the list, so that `dishes` can be changed without `data[1]` also changing
dishes = data[1][:]

# create empty shopping list (will be a list of lists)
shopping_list = []

# to test for duplicates
shopping_list.append(['flour (g)', 60.25])
shopping_list.append(['butter (g)', 100.0])

# select a dish – this will be done by user input in the final version
selected_dish = data[1][4]

# remove the selected dish from the list of available dishes
dishes.remove(selected_dish)

def get_ingredients(selection):
    """Get list of ingredients for a selected dish, add them to `shopping_list`, return a list of lists"""
    print(selection)
    # get the index of the selected dish
    selection_index = data[1].index(selection)
    # go through each row
    for row in data:
        # if the cell in the row under the selected dish has content (ingredient quantity)
        # and it's not one of the first 2 rows
        if row[selection_index] and data.index(row) > 1:
            # print the ingredient name and amount
            print(row[0]+' '+row[selection_index])
            # add the list of ingredient + quantity to the list of ingredients (converted to a float)
            shopping_list.append([row[0], float(row[selection_index])])
    return shopping_list

def unify_ingredients():
    """Check `shopping_list` for pairs of items (lists) where the ingredient is the same.
    Add quantities of the ingredient together.
    Return modified `shopping_list`."""
    # this needs to be run every time items are added to `shopping_list`
    shopping_list = get_ingredients(selected_dish)
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
    return shopping_list

for i in range(1, len(dishes)):
    print(i,dishes[i])


for i in range(1, len(data[1])):
    print(i,data[1][i])


print(unify_ingredients())

