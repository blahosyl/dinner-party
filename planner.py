# This module provides objects and methods for planning dinner parties

# STANDARD PACKAGES

# import sleep to show output for some time period
# package suggested by my mentor
from time import sleep

# 3RD PARTY LIBRARIES

# get combinations from a list
import itertools

# colored terminal output
# package suggested by my mentor
from colorama import Fore, Back

# SELF-WRITTEN MODULES & FUNCTIONS

# general-purpose functions
from utilities import validate_range, clear


class DishList:
    """
    Creates an instance of DishList
    """

    def __init__(self, dish_data):
        self.dish_data = dish_data

    def print_enum(self):
        """
        Print available dishes in a numbered list
        """
        # sort list alphabetically
        self.dish_data.sort()
        # print an empty line to visually separate the list
        print('\n')
        # for each item starting from 1 (not 0), print its index (in green)
        # and the item
        for i in range(1, len(self.dish_data)):
            print(Fore.GREEN + str(i) + Fore.RESET, self.dish_data[i])
        # print an empty line to visually separate the list
        print('\n')

    def select_dish(self):
        # print the list of dishes in a numbered list
        self.print_enum()

        # validating the input
        text = [Back.MAGENTA + 'Type in the '
                + Fore.GREEN + 'number ' + Fore.RESET
                + "of the dish you'd like to add:"
                + Back.RESET + ' ']
        dish_number = \
            validate_range(text, int, 1, len(self.dish_data) - 1)

        # get the dish with the selected number from the `dishes` list
        selected_dish = self.dish_data[int(dish_number)]

        # print the selected dish's name
        print(f'\nYou have selected: {selected_dish}')
        # sleep for 1.5 seconds after printing output
        sleep(0.5)
        # clear the console
        clear()

        # remove the selected dish from the list of available dishes
        self.dish_data.remove(selected_dish)

        return selected_dish


def parse_string(ingredient_string):
    """
    Find the abbreviation string,
    replace it with the full unit name
    if it is in the dictionary
    The input string must contain ( and )
    :param ingredient_string: string
    :return: list[opening parenthesis index,
                    abbreviation,
                    Boolean: abbr in dictionary or not,
                    modified intput string]
    """
    # abbreviations and corresponding unit names
    units = {
        'g': 'grams',
        'kg': 'kilograms',
        'pc': 'pieces',
        'ml': 'milliliters',
        'l': 'liters',
        'Tbsp': 'tablespoons',
        'cloves': 'cloves',
    }
    # find the index of the opening bracket in the string
    opening = ingredient_string.index('(')
    # replace measurement unit abbreviation with full name
    # get the substring between the opening and the closing bracket
    abbr = ingredient_string[opening:].partition(')')
    # get the first item (opening bracket plus abbreviation)
    abbr = abbr[0]
    # delete the opening bracket from the variable
    abbr = abbr.replace('(', '')
    # if the abbreviation is in the `units` dictionary,
    # replace it with the corresponding unit name
    if abbr in units:
        unit_name = units[abbr]
        in_dict = True
    # if it's not in the dictionary, leave it as is
    else:
        unit_name = abbr
        in_dict = False
    # replace a parenthesis+abbreviation with parenthesis+unit name
    # need to specify parenthesis as well, so that it does not
    # replace things like "g" across the board (unintended)
    ingredient_string = ingredient_string.replace('(' + abbr, '(' + unit_name)
    return [opening, unit_name, in_dict, ingredient_string]


def print_formatted(ingredient_list):
    """ Print ingredient list in a user-friendly string format"""
    # print an empty line to visually separate the block
    print('\n')
    # for every item in the list
    for i in range(0, len(ingredient_list)):
        # set `print_string` as the first item of the list
        print_string = ingredient_list[i][0]
        quantity = ingredient_list[i][1]

        # replace unit abbreviation with full name
        parsed_string = parse_string(print_string)
        # index of the opening parenthesis
        opening = parsed_string[0]
        unit_name = parsed_string[1]
        in_dict = parsed_string[2]
        print_string = parsed_string[3]
        # if the quantity is exactly 1, and it's in the dictionary
        if quantity == 1 and in_dict:
            # make unit_name singular (remove string-final 's')
            print_string = print_string.replace(unit_name, unit_name[:-1])
        # end of code to replace measurement abbreviation with full name

        # 1 left of the opening bracket, add the following:
        # a colon
        # the quantity (second item of the list)
        # in general notation
        print_string = print_string[:opening - 1] \
                       + ': ' \
                       + f'{quantity:g}' \
                       + print_string[opening - 1:]
        # delete the opening and closing parenthesis
        print_string = print_string.replace('(', '')
        print_string = print_string.replace(')', '')
        print(Fore.GREEN + print_string + Fore.RESET)


class ShoppingList:
    """
        Creates an instance of ShoppingList
        """

    def __init__(self, list_data):
        self.list_data = list_data

    def get_ingredients(self, selection, recipe_data):
        """Get list of ingredients for a selected dish, print them out,
        add them to the shopping list, return a list of lists
        """

        print(Fore.GREEN + f'\nIngredients for {selection}' + Fore.RESET)
        # get the index of the selected dish in the database
        selection_index = recipe_data[1].index(selection)
        # the list of ingredients for the selected dish
        dish_ingredients = []
        # go through each row
        for row in recipe_data:
            # if the cell in the row under the selected dish has content
            # (ingredient quantity)
            # and it's not one of the first 2 rows
            if row[selection_index] and recipe_data.index(row) > 1:
                # add the list [ingredient, quantity(converted to a float)]
                # to the shopping list
                dish_ingredients.append([row[0], float(row[selection_index])])
        # sort list alphabetically
        dish_ingredients.sort()
        # print the ingredients for the selected dish
        print_formatted(dish_ingredients)
        # add each ingredient from the selected dish to the shopping list
        for ingredient in dish_ingredients:
            self.list_data.append(ingredient)
            # sort list alphabetically
            self.list_data.sort()
        return self.list_data

    def unify_ingredients(self, selection, recipe_data):
        """Check shopping list for pairs of items (lists)
        where the ingredient is the same.
        Add quantities of the ingredient together.
        Return modified shopping list."""
        # this needs to be run every time items are added to the shopping list
        self.list_data = self.get_ingredients(selection, recipe_data)
        # get all pairs of items within the shopping list item
        for x, y in itertools.combinations(self.list_data, 2):
            # if the ingredient name and unit (first item of both lists)
            # is the same
            if x[0] == y[0]:
                # TESTING: print for testing/development
                # print pairs of items where the ingredient is the same
                # print(x, y)
                # add a new item (list)
                # with this ingredient name and unit as its first item,
                # and the sum of the two quantities as the second item
                self.list_data.append([x[0], x[1] + y[1]])
                # remove the two original items from shopping list
                self.list_data.remove(x)
                self.list_data.remove(y)
        print('\nShopping list updated ✅\n')
        # ask_more()
        return self.list_data
