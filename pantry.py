shopping_list = [
    ["lemon (pc)", 3],
    ["olives (g)", 10],
    ["tahini (Tbsp)", 4],
]
# create an intermediate list to store ingredients where quantity is more than 0
# this is needed because removing items from a list in a loop causes "index out of range" issues
# list comprehension also doesn't work well with list of lists
revised_list = []
# for each item on the shopping list
for i in range(0, len(shopping_list)):
    # ask how much the user has
    have = float(input(f"How much {shopping_list[i][0]} do you have?"))
    # deduct the quantity in the pantry from the quantity on the shopping list
    shopping_list[i][1] -= have
    # if the resulting quantity is more than 0
    if shopping_list[i][1] > 0:
        # add the whole item to the new intermediate list
        revised_list.append(shopping_list[i])
#  set the contents of the shopping list to the intermediate list
shopping_list = revised_list

print(shopping_list)

