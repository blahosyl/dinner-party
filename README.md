

[Go to the deployed app](https://dinner-party-planner-ee795b43bd35.herokuapp.com/)


## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Flow

![Program flowchart](readme-pics/dinner-party-flow.jpg)

### CRUD functionalities

Create

- dataset from Google Sheets
- list of dishes
- shopping list

Read
- dataset from Google Sheets
- list of dishes
- shopping list
- ingredients of a dish

Update
- list of dishes
- shopping list

Delete
- items from the shopping list


## Database

[Google Sheet](https://docs.google.com/spreadsheets/d/1LgNPD9jQ0_7QM3arULAzwTUS3EMnfB1aXBNsTJC_POQ/edit?usp=sharing)

## Deployment to Heroku

1. Create a list of requirements by going to the terminal and typing `pip3 freeze > requirements.txt`. This popuplates your `requirements.txt` file with the list of required files.<br> 
Push your changes to GitHub.
2. Under **Settings > Config Vars** in Heroku, add  a new var  with the key `CREDS` and the value equal to the contents of your `creds.json` file.
3. Under **Settings > Config Vars** in Heroku, add  a new var  with the key  `PORT` witht the key `PORT` and the value `8000`.
4. Under **Settings > Buildpacks** in Heroku, add Python to Heroku Buildpacks.
5. Under **Settings > Buildpacks** in Heroku, add NodeJS to Heroku Buildpacks.
6. Under **Deploy > Deployment method** in Heroku, select **GitHub** and connect Heroku to your GitHub account.<br>
Type in your repository name, then click **Search**. When your repository appears, click **Connect** next to it.
7. Under **Deploy > Manual deploy** in Heroku, select **Deploy branch** to deploy manually.<br>
Once the process is finished, the following message will appear:<br>
_Your app was successfully deployed_<br>
Click **View** under the message, and a new tab will appear with your deployed app.
8. (optional) Under **Deploy > Automatic deploy** in Heroku, select **Enable Automatic Deploys** if your want your app to be rebuild each time you push to the `main` branch of your GitHub repository.

## Technologies used

### Languages

Python

#### External libraries

Which libraries are used and what their purpose is, why they are needed

## Testing

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


## Credits

### Study/lookup sources

The following resources were used to learn/double check general, atomic functionalities/syntax:

- [`gspread` user guide](https://docs.gspread.org/en/v6.0.0/user-guide.html)
- [Copy list so it can be changed without affecting the original list](https://stackoverflow.com/a/25004389)
- [Remove item from list](https://www.w3schools.com/python/python_lists_remove.asp)
- [Docstring conventions](https://peps.python.org/pep-0257/)
- [Get combinations of items from a list](https://stackoverflow.com/a/16603347)
- [`itertools` package documentation](https://docs.python.org/3/library/itertools.html#itertools.combinations)
- [Add list items](https://www.w3schools.com/python/python_lists_add.asp)
- [Remove specified item from a list](https://www.w3schools.com/python/python_lists_remove.asp)
- [Docstring conventions](https://peps.python.org/pep-0257/)
- [Check if a string is empty](https://stackoverflow.com/a/9573259)
- [Convert `input` to `int` with `Try/Except`](https://www.tutorialsteacher.com/articles/convert-input-to-number-in-python)
- [`try`/`except`](https://www.w3schools.com/python/python_try_except.asp)
- [Errors and exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Input validation: integer in range (did not work)](https://stackoverflow.com/questions/11594605/python-excepting-input-only-if-in-range)
- [insert a substring before/after a certain characted in a string](https://stackoverflow.com/a/30232424/24248624)
- [delete a character from a string](https://builtin.com/software-engineering-perspectives/python-remove-character-from-string)
- [fix `TERM environment variable not set` error](https://stackoverflow.com/a/65161315/24248624)
- [clear the terminal](https://www.geeksforgeeks.org/clear-screen-python/)
- [naming conventions](https://peps.python.org/pep-0008/)
- [naming global vs. local variables](https://stackoverflow.com/questions/69193413/why-does-the-python-style-guide-suggest-the-same-style-for-both-global-and-local)
- [conventions for putting modules into separate files](https://stackoverflow.com/questions/2864366/are-classes-in-python-in-different-files)
- [classes of the same module can be grouped in the same file](https://softwareengineering.stackexchange.com/a/306492)
- [print floats in general notation - only print decimal point and decimal place digits if they are "not empty"](https://stackoverflow.com/a/2440708/24248624)
- [string operations](https://docs.python.org/3/library/string.html#format-specification-mini-language)
- [cut off last character of string](https://stackoverflow.com/a/15478161/24248624)
- [regular expression for letters (not used)](https://stackoverflow.com/a/3617808/24248624)
- [`partition` method example ](https://stackoverflow.com/a/54608451/24248624)
- [`partition` method on W3Schools](https://www.w3schools.com/python/ref_string_partition.asp)
- [`colorama` documentation](https://pypi.org/project/colorama/)
- [escaping characters in ACII art](https://code-institute-room.slack.com/archives/C027C3S3TEU/p1636456674153400?thread_ts=1636388878.151000&cid=C027C3S3TEU
)
- [string literals with `r`](https://stackoverflow.com/a/4780104/24248624)

### Code

The following sources contributed code or suggestions to specific functions within the project:

- Rory Patrick Sheridan, my mentor, gave suggestions, helped me solve or spotted bugs described in [these Issues](https://github.com/blahosyl/dinner-party/issues?q=is%3Aissue+label%3Amentor) (see the Issue descriptions and comments for details).


### Content

All text content was written by me.

### Media

#### Images

### Readme

- [Creating your first README with Kera Cudmore](https://www.youtube.com/watch?v=XbYJ4VlhSnY) by Code Institute
- [Creating your first README](https://github.com/kera-cudmore/readme-examples) by Kera Cudmore
- [Bully Book Club](https://github.com/kera-cudmore/Bully-Book-Club) by Kera Cudmore
- [Bodelschwingher Hof](https://github.com/4n4ru/CI_MS1_BodelschwingherHof/tree/master) by Ana Runje
- [Travel World](https://github.com/PedroCristo/portfolio_project_1/) by Pedro Cristo
- [Sourdough Bakes](https://github.com/siobhanlgorman) by Siobhan Gorman
- [Horizon Photo](https://github.com/Ri-Dearg/horizon-photo/blob/master/README.md#mobile-testing) by Rory Patrick Sheridan
- [The README of my first Code Institute project](https://github.com/blahosyl/academic-publishing)
