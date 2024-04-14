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
