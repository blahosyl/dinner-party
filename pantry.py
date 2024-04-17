# STANDARD PACKAGES

from time import sleep

# 3RD PARTY LIBRARIES

from colorama import Fore, Back, Style

# SELF-WRITTEN MODULES & FUNCTIONS

# import this module for classes custom written for this project
import planner

shopping_list = planner.ShoppingList([
    ["lemon (pc)", 3],
    ["olives (g)", 10],
    ["tahini (Tbsp)", 4],
])


def check_pantry():
    # create an intermediate list to store ingredients where quantity
    # is more than 0
    # this is needed because removing items from a list in a loop causes
    # "index out of range" issues
    # list comprehension also doesn't work well with list of lists
    revised_list = []
    # for each item on the shopping list
    for i in range(0, len(shopping_list.list_data)):

        # parse ingredient text, replace measurement abbreviation
        # with full unit name
        parsed_text = planner.parse_string(shopping_list.list_data[i][0])

        # the index of the opening parenthesis
        opening = parsed_text[0]
        # the full name of the measurement unit
        unit_name = parsed_text[1]

        # the ingredient string ("ingredient (measurement)")
        ingredient_text = parsed_text[3]
        # delete string content starting from the space
        # before the opening parenthesis
        ingredient_text = ingredient_text[:opening - 1]

        # ask how much of the given ingredient the user has
        text = [f'{Style.BRIGHT}How many {Fore.MAGENTA}{unit_name}{Fore.RESET} '
                f'of {Fore.GREEN}{ingredient_text}{Fore.RESET} '
                f'do you have?\n'
                f'{Back.MAGENTA}Type {Fore.GREEN}0{Fore.RESET} '
                f'if you don\'t have any{Back.RESET} ']
        # get and validate the input (float, >=0, no upper limit)
        have = planner.validate_range(text, float, 0)
        print(f'Got it, you have {have:g} {unit_name} of {ingredient_text}\n')
        # sleep for 0.5 seconds after printing output
        sleep(0.5)

        # deduct the quantity in the pantry from the quantity on the shopping list
        shopping_list.list_data[i][1] -= have
        # if the resulting quantity is more than 0
        if shopping_list.list_data[i][1] > 0:
            # add the whole item to the new intermediate list
            revised_list.append(shopping_list.list_data[i])
    #  set the contents of the shopping list to the intermediate list
    shopping_list.list_data = revised_list

    print('\nAll done checking your pantry! 🎉\n'
          'Here comes your revised shopping list 📋')

    # sleep for 1.5 seconds after printing output
    sleep(1.5)
    planner.print_formatted(shopping_list.list_data)


check_pantry()

