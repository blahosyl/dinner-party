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
print(data)

# row 0 is the type of dish: starter, main, dessert or drink
# row 1 of `data` is the list of dishes
# item 0 of each row is the ingredient
# subsequent items of each row are the quantity of ingredients needed for the corresponding dish
# when an ingredient is not needed for a dish, the corresponding cell is empty

# create empty shopping list (will be a list of lists)
shopping_list = []

# select a dish – this will be done by user input in the final version
selected_dish = data[1][4]

# Get list of ingredients for a selected dish
def get_ingredients(selection):
    print(selected_dish)
    # empty list of ingredients
    ingredient_list = []
    # get the index of the selected dish
    selection_index = data[1].index(selection)
    # go through each row
    for row in data:
        # if the cell in the row under the selected dish has content (ingredient quantity)
        if row[selection_index] and data.index(row) > 1:
            # print the ingredient name and amount
            print(row[0]+' '+row[selection_index])
            ingredient_list.append([row[0],row[selection_index]])
    return ingredient_list

shopping_list.append(get_ingredients(selected_dish))

print(shopping_list)

