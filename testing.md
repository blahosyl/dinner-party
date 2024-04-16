This document describes the testing procedures for the [Dinner Party app](README.md).

## User story testing

## Code validation

### Naming conventions used

- all class names are in `CamelCase`.
- all constant names are in `ALL_CAPS`.
- all variable names are in `snake_case`.
- following my mentor's suggestion, I changed the names of global variables (that are not constants) so that they always start with an underscore: `_global_variable`.

### PIP8 validation

###HTML/CSS validation


## User input validation

### Y/N questions

#### Initial question


`Would you like to plan a dinner party? (Y/N):`

#### Single-step test cases


|Input						|Expected answer	|Result|
|---						|---				|---	|
|other letter character	|I did not understand. Please type Y or N:| |
|special character	|I did not understand. Please type Y or N:| |
|space	|I did not understand. Please type Y or N:| |
|empty string	|I did not understand. Please type Y or N:| |
|number character	|I did not understand. Please type Y or N:| |
|`Y` or `y`			|Here is the list of dishes you can choose from.| |
|`N` or `n`			|Maybe some other time, then.| |


#### Double-step test cases


|Shorthand	| Stands for|
|---			|---		|
|`Y`			|	`Y` or `y`	|
|`N`			|	`N` or `n`	|
|`X`			| Any other character|



|Input						|Expected answer	|Result|
|---						|---				|---	|
|`X` then `X`		|I did not understand[...] x2| |
|`X` then `Y`		|I did not understand[...] Here is the list of dishes[...]| |
|`X` then `N`		|I did not understand[...] Maybe some other time, then.| |
|`Y` then `Y`		|*not possible, program continues after 1st input*| |
|`Y` then `X`		|*not possible, program continues after 1st input*| |
|`Y` then `N`		|*not possible, program continues after 1st input*| |
|`N` then `N`		|*not possible, program continues after 1st input*| |
|`N` then `X`		|*not possible, program continues after 1st input*| |
|`N` then `Y`		|*not possible, program continues after 1st input*| |

#### Add more dishes question


`Would you like to add another dish? (Y/N):`

#### Single-step test cases


|Input						|Expected answer	|Result|
|---						|---				|---	|
|other letter character	|I did not understand. Please type Y or N:| |
|special character	|I did not understand. Please type Y or N:| |
|space	|I did not understand. Please type Y or N:| |
|empty string	|I did not understand. Please type Y or N:| |
|number character	|I did not understand. Please type Y or N:| |
|`Y` or `y`			|Cool, here is the list of dishes again:| |
|`N` or `n`			|Got it! That's all for now, then.| |

#### Double-step test cases


|Shorthand	| Stands for|
|---			|---		|
|`Y`			|	`Y` or `y`	|
|`N`			|	`N` or `n`	|
|`X`			| Any other character|



|Input						|Expected answer	|Result|
|---						|---				|---	|
|`X` then `X`		|I did not understand[...] x2| |
|`X` then `Y`		|I did not understand[...] Cool, here is the list of dishes again:| |
|`X` then `N`		|I did not understand[...] Got it! That's all for now, then.| |
|`Y` then `Y`		|*not possible, program continues after 1st input*| |
|`Y` then `X`		|*not possible, program continues after 1st input*| |
|`Y` then `N`		|*not possible, program continues after 1st input*| |
|`N` then `N`		|*not possible, program continues after 1st input*| |
|`N` then `X`		|*not possible, program continues after 1st input*| |
|`N` then `Y`		|*not possible, program continues after 1st input*| |


### Integer from a range

#### Single-step test cases


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

#### Double-step test cases

|Shorthand	| Stands for|
|---			|---		|
|`INT`✅	|integer from the range	|
|`INT`❌	|integer from outside the range|
|`X`			| Any other character|



|Input						|Expected answer	|Result|
|---						|---				|---
|`X` then `X`				|That is not a valid number[...] x2| |
|`X` then `INT`❌		|That is not a valid number[...] Number out of range[...]| |
|`X` then `INT`✅		|That is not a valid number[...] You have selected[...]| |
|`INT`❌ then `INT`❌	|Number out of range[...] x2 | |
|`INT`❌ then `X`		|Number out of range[...] That is not a valid number[...] | |
|`INT`❌ then `INT`✅		|Number out of range[...]  You have selected[...]| |
|`INT`✅ then `INT`✅		|*not possible, program continues after 1st input*| |
|`INT`✅ then `X`		|*not possible, program continues after 1st input*| |
|`INT`✅ then `INT`❌		|*not possible, program continues after 1st input*| |


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

### Database data validation (to be automated)

Check if ingredient cell contains `(`