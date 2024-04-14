# This module provides objects and methods for planning dinner parties

# get combinations from a list
import itertools


class DishList:
    """
    Creates an instance of DishList
    """

    def __init__(self, dish_data):
        self.dish_data = dish_data

    def print_enum(self):
        # print an empty line to visually separate the list
        print('\n')
        """ Print available dishes """
        for i in range(1, len(self.dish_data)):
            print(i, self.dish_data[i])
        # print an empty line to visually separate the list
        print('\n')

    def select_dish(self):
        # print the list of dishes in a numbered list
        self.print_enum()

        # validating the input
        while True:
            try:
                # ask user to select a dish number
                dish_number = int(input("Type in the number of the dish you'd like to add: "))
                while dish_number < 1 or dish_number > len(self.dish_data) - 1:
                    dish_number = int(
                        input(f"Number out of range. Please type a number between 1 and {len(self.dish_data) - 1}: "))
                break
            except ValueError:
                # while the input is not one of the allowed options
                # ask for input again
                print(f"That is not a valid number. "
                      f"Please type a whole number between 1 and {len(self.dish_data) - 1}.")

        # get the dish with the selected number from the `dishes` list
        selected_dish = self.dish_data[int(dish_number)]

        # print the selected dish's name
        print(f'\n You have selected: {selected_dish}')

        # remove the selected dish from the list of available dishes
        self.dish_data.remove(selected_dish)

        return selected_dish


class ShoppingList:
    """
        Creates an instance of ShoppingList
        """
    def __init__(self, list_data):
        self.list_data = list_data

    def print_formatted(self, ingredient_list):
        """ Print ingredient list in a user-friendly string format"""
        # print an empty line to visually separate the list
        print('\n')
        for i in range(0, len(ingredient_list)):
            # print(shopping_list[i][0], shopping_list[i][1])
            print_string = ingredient_list[i][0]
            opening = print_string.index('(')
            print_string = print_string[:opening-1] + ': ' + str(ingredient_list[i][1]) + print_string[opening-1:]
            print_string = print_string.replace('(', '')
            print_string = print_string.replace(')', '')
            print(print_string)
        # print an empty line to visually separate the list
        print('\n')

    def get_ingredients(self, selection, recipe_data):
        """Get list of ingredients for a selected dish, print them out,
        add them to the shopping list, return a list of lists
        """

        # print an empty line to visually separate the block
        print('\n')
        print(f'Ingredients for {selection}')
        # get the index of the selected dish in the database
        selection_index = recipe_data[1].index(selection)
        # the list of ingredients for the selected dish
        dish_ingredients = []
        # go through each row
        for row in recipe_data:
            # if the cell in the row under the selected dish has content (ingredient quantity)
            # and it's not one of the first 2 rows
            if row[selection_index] and recipe_data.index(row) > 1:
                # add the list [ingredient, quantity(converted to a float)] to the shopping list
                dish_ingredients.append([row[0], float(row[selection_index])])
        # print the ingredients for the selected dish
        self.print_formatted(dish_ingredients)
        # add each ingredient from the selected dish to the shopping list
        for ingredient in dish_ingredients:
            self.list_data.append(ingredient)
        # print an empty line to visually separate the block
        print('\n')
        return self.list_data

    def add_ingredients(self, selection, recipe_data):
        """Check shopping list for pairs of items (lists) where the ingredient is the same.
        Add quantities of the ingredient together.
        Return modified shopping list."""
        # this needs to be run every time items are added to the shopping list
        self.list_data = self.get_ingredients(selection, recipe_data)
        # get all pairs of items within the shopping list item
        for x, y in itertools.combinations(self.list_data, 2):
            # if the ingredient name and unit (first item of both lists) is the same
            if x[0] == y[0]:
                # TESTING: print for testing/development
                print(x, y)
                # add a new item (list) with this ingredient name and unit as its first item,
                # and the sum of the two quantities as the second item
                self.list_data.append([x[0], x[1] + y[1]])
                # remove the two original items from shopping list
                self.list_data.remove(x)
                self.list_data.remove(y)
        print('Shopping list updated\n')
        # ask_more()
        return self.list_data
