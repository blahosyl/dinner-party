class DishList:
    """
    Creates an instance of DishLish
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


dishes = DishList(["biscuits", "tea", "dip"])

dishes.print_enum()
