shopping_list = [
    ["lemon (pc)", 3],
    ["olives (g)", 10],
    ["tahini (Tbsp)", 4],
]

for i in range(0, len(shopping_list)):
    have = float(input(f"How much {shopping_list[i][0]} do you have?"))
    shopping_list[i][1] -= have

print(shopping_list)
