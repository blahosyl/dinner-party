This document describes the testing procedures for the [Dinner Party app](README.md).

## User story testing

## Code validation

### Naming conventions used

- all class names are in `CamelCase`.
- all constant names are in `ALL_CAPS`.
- all variable names are in `snake_case`.
- following my mentor's suggestion, I changed the names of global variables (that are not constants) so that they always start with an underscore: `_global_variable`.


## User input validation

### Y/N questions

#### Initial question


`Would you like to plan a dinner party? (Y/N):`


|Input						|Expected answer	|Result|
|---						|---				|---	|
|other letter character	|I did not understand. Please type Y or N:| |
|special character	|I did not understand. Please type Y or N:| |
|space	|I did not understand. Please type Y or N:| |
|empty string	|I did not understand. Please type Y or N:| |
|number character	|I did not understand. Please type Y or N:| |
|`Y` or `y`			|Here is the list of dishes you can choose from.| |
|`N` or `n`			|Maybe some other time, then.| |

#### Add more dishes question


`Would you like to add another dish? (Y/N):`


|Input						|Expected answer	|Result|
|---						|---				|---	|
|other letter character	|I did not understand. Please type Y or N:| |
|special character	|I did not understand. Please type Y or N:| |
|space	|I did not understand. Please type Y or N:| |
|empty string	|I did not understand. Please type Y or N:| |
|number character	|I did not understand. Please type Y or N:| |
|`Y` or `y`			|Cool, here is the list of dishes again:| |
|`N` or `n`			|Got it! That's all for now, then.| |

### Integer from a range


`Type in the number of the dish you'd like to add:`


|Input						|Expected answer	|Result|
|---						|---				|---	|
|letter character	|That is not a valid number. Please type a whole number between 1 and `<range>`.| |
|special character	|That is not a valid number. Please type a whole number between 1 and `<range>`.| |
|space	|That is not a valid number. Please type a whole number between 1 and `<range>`.| |
|empty string	|That is not a valid number. Please type a whole number between 1 and `<range>`.| |
|non-integer number	|That is not a valid number. Please type a whole number between 1 and `<range>`.| |
|integer outside the range	|Number out of range. Please type a number between 1 and `<range>`:| |
|integer from the specified range	|You have selected: `<dish>`| |





Combinations:

- integer outside the range THEN non-number character
- non-number character THEN integer outside the range

## Flow testing

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

### Database data validation (optional)

Check if ingredient cell contains `(`