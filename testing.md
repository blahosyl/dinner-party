This document describes the testing procedures for the [Dinner Party app](README.md).

### User story testing

### Code validation

#### Naming conventions used

- all class names are in `CamelCase`.
- all constant names are in `ALL_CAPS`.
- all variable names are in `snake_case`.
- following my mentor's suggestion, I changed the names of global variables (that are not constants) so that they always start with an underscore: `_global_variable`.


### User input

#### Y/N questions

- `Y` or `N` – correct
- `y` or `n`
- empty string
- space
- special character
- other letter character
- number character

#### Integer from a range

- integer from the specified range – correct
- integer outside the range
- non-integer number
- empty string
- space
- special character
- letter character

Combinations:

- integer outside the range THEN non-number character
- non-number character THEN integer outside the range

### Flow testing

- if the user answers `N` to the 1st question: end with message
- if the user selects a dish:
	- remove it from the list of dishes
	- display its name and ingredients
	- add its ingredients to the shopping list
- if the shopping list already contains an ingredient that is added: combine two items into one, sum the ingredient quantity
- if the user wants to continue adding an ingredient: rerun adding loop
- if the user does not want to  add more ingredients: 
	- display shopping list
	- end adding loop
	- display goodbye message
- if the user selects all dishes: 
	- print shopping list 
	- end program

#### Database data validation (optional)

Check if ingredient cell contains `(`