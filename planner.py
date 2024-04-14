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
                print(f"That is not a valid number. Please type a whole number between 1 and {len(self.dish_data) - 1}.")

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

    def print_string(self):
        """ Print shopping list in a user-friendly string format"""
        # print an empty line to visually separate the list
        print('\n')
        for i in range(0, len(self.list_data)):
            # print(shopping_list[i][0], shopping_list[i][1])
            print_string = self.list_data[i][0]
            opening = print_string.index('(')
            print_string = print_string[:opening-1] + ': ' + str(self.list_data[i][1]) + print_string[opening-1:]
            print_string = print_string.replace('(', '')
            print_string = print_string.replace(')', '')
            print(print_string)
        # print an empty line to visually separate the list
        print('\n')

    def get_ingredients(self, selection, data):
        """Get list of ingredients for a selected dish, print them out,
        add them to the shopping list, return a list of lists
        """

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
                self.list_data.append([row[0], float(row[selection_index])])
        # print an empty line to visually separate the block
        print('\n')
        return self.list_data


#   def add_ingredients()


shopping_list = ShoppingList([])

data = [['', 'starter', 'starter', 'starter', 'starter', 'starter', 'main', 'main', 'main', 'dessert', 'dessert', 'dessert', 'drink', 'drink', 'drink'], ['', 'céklás tormás', 'Tahini lemon dip', 'Tapenade green', 'Parmezános keksz', 'majonézes karalábé', 'risotto', 'frittata', 'pumpkin quiche', 'red velvet cake', 'lemon bar', 'Vegan Lemon Cake', 'Daiquiry mix', 'bloody mary', 'Pitcher Margarita'], ['risotto rice (g)', '', '', '', '', '', '500', '', '', '', '', '', '', '', ''], ['baking soda (g)', '', '', '', '', '', '', '', '', '2.5', '', '', '', '', ''], ['beetroot, raw (g)', '400', '', '', '', '', '', '', '', '240', '', '', '', '', ''], ['lemon (pc)', '', '1', '', '', '', '', '', '', '1', '2', '1', '', '', '2'], ['Cointreau (ml)', '', '', '', '', '', '', '', '', '', '', '', '', '', '250'], ['creme fraiche (ml)', '200', '', '', '', '', '', '', '', '450', '', '450', '', '', ''], ['white wine (ml)', '', '', '', '', '', '250', '', '', '', '', '', '', '', ''], ['garlic clove (pc)', '', '', '', '', '', '3', '', '', '', '', '', '', '', ''], ['tofu, smoked (g)', '', '', '', '', '', '', '200', '', '', '', '', '', '', ''], ['onion (pc)', '', '', '', '', '', '1', '', '', '', '', '', '', '', ''], ['cocoa powder (g)', '', '', '', '', '', '', '', '', '45', '', '', '', '', ''], ['capers (Tbsp)', '', '', '1', '', '1', '', '', '', '', '', '', '', '', ''], ['kohlrabi (pc)', '', '', '', '', '1', '', '', '', '', '', '', '', '', ''], ['blue cheese (g)', '', '', '', '', '', '', '', '100', '', '', '', '', '20', ''], ['lime (pc)', '', '', '', '', '', '', '', '', '', '', '', '7', '', '4'], ['flour (g)', '', '', '', '200', '', '', '', '', '240', '300', '240', '', '', ''], ['mayonnaise (ml)', '', '', '', '', '180', '', '', '', '', '', '', '', '', ''], ['maple syrup (ml)', '', '30', '', '', '', '', '', '', '', '', '15', '', '', ''], ['mini mozarella (g)', '', '', '', '', '', '', '', '', '', '', '', '', '125', ''], ['gherkins (ml)', '', '', '', '', '', '', '', '', '', '', '', '', '100', ''], ['milk (ml)', '', '', '', '', '', '', '', '300', '', '', '150', '', '', ''], ['olive oil (ml)', '', '', '', '', '', '', '', '', '', '', '130', '', '', ''], ['tomato juice (ml)', '', '', '', '', '', '', '', '', '', '', '', '', '1000', ''], ['parmiggiano (g)', '', '', '', '200', '', '100', '', '', '', '', '', '', '', ''], ['sugar (g)', '', '', '', '', '', '', '', '', '375', '400', '', '', '', ''], ['carrots (pc)', '', '', '', '', '', '1', '', '', '', '', '', '', '', ''], ['rum (ml)', '', '', '', '', '', '', '', '', '', '', '', '300', '', ''], ['simple syrup (ml)', '', '', '', '', '', '', '', '', '', '', '', '60', '', ''], ['sütőpor (g)', '', '', '', '', '', '', '', '', '6', '5', '', '', '', ''], ['hokkaido squash (pc)', '', '', '', '', '', '', '', '1', '', '', '', '', '', ''], ['tahini (ml)', '', '100', '', '', '', '', '', '', '', '', '', '', '', ''], ['tequila (ml)', '', '', '', '', '', '', '', '', '', '', '', '', '', '375'], ['eggs (db)', '', '', '', '', '', '', '6', '5', '4', '4', '', '', '', ''], ['horseradish, fresh (pc)', '1', '', '', '', '', '', '', '', '', '', '', '', '', ''], ['hazelnuts (g)', '', '', '', '', '', '', '', '150', '', '', '', '', '', ''], ['butter (g)', '', '', '', '150', '', '', '', '150', '172.5', '250', '', '', '', ''], ['vanilla extract (ml)', '', '', '', '', '', '', '', '5', '7.5', '', '', '', '', ''], ['yoghurt (ml)', '', '', '', '', '', '', '', '', '', '', '130', '', '', ''], ['double cream (ml)', '', '', '', '', '', '', '', '300', '', '', '', '', '', ''], ['oat flakes (g)', '', '', '', '', '', '', '', '200', '', '', '', '', '', ''], ['green olives (g)', '', '', '150', '', '', '', '', '', '', '', '', '', '100', ''], ['sage (g)', '', '', '', '', '', '', '', '15', '', '', '', '', '', '']]


shopping_list.get_ingredients("red velvet cake", data)

shopping_list.get_ingredients("risotto", data)