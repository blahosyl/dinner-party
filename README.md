# Dinner Party Planner

This app helps plan dinner parties by managing a recipe database, creating shopping lists, and cshecking off items already in your pantry | CodeInstitute Portfolio Project 3


Developer: [Dr. Sylvia Blaho](https://www.linkedin.com/in/blahosylvia/)


![Deployed site starting screen](assets/readme-pics/start-screen-full.png)


[Go to the deployed app](https://dinner-party-planner-ee795b43bd35.herokuapp.com/)

See the development progress and further plans on [GitHub Projects](https://github.com/users/blahosyl/projects/1/views/2).

<!--Shield.io badges-->

![GitHub last commit](https://img.shields.io/github/last-commit/blahosyl/operator-game?color=red)
![GitHub contributors](https://img.shields.io/github/contributors/blahosyl/operator-game?color=orange)
![GitHub language count](https://img.shields.io/github/languages/count/blahosyl/operator-game?color=black)

## Table of Contents

## User Experience (UX)

### User goals

### Creator goals

## Design

### Flow

![Program flowchart: initial plan](assets/readme-pics/initial-flow-dinner-party.jpg)

The current version of the program flow is as follows ([click here to view the full-size version on Mire](https://miro.com/app/board/uXjVKVLz2oI=/?share_link_id=420958715421)):

![Program flowchart: initial plan](assets/readme-pics/current-flow-dinner-party.jpg)


#### CRUD functionalities

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


### Database

[Google Sheet](https://docs.google.com/spreadsheets/d/1LgNPD9jQ0_7QM3arULAzwTUS3EMnfB1aXBNsTJC_POQ/edit?usp=sharing)

A new test account was created for this purpose, for security reasons.

### Visual design of the terminal

#### Pause

#### Clear screen

#### ASCII art

#### Color

The main colors chosen (magenta and green) harmonize with the [background image](#background-image) of the site.

In addition, red is used for validation messages.

However, the use of color in this project goes beyond aesthetic purposes: it also serves to aid the user experience, and is deliberately used to distinguish different functional elements from each other:

|style					|function|
|---					|---|
|colored backgroud 	|user input needed |
|red				 	|user entered invalid data|
|green test			|information that the user needs to proceed|
|magenta ASCII text	|start and end of progam|


### Website design

As this project is focused on Python rather than HTML/CSS, designing/altering the site itself was an optional extra.

Nevertheless, I chose to lightly alter the provided HTML/CSS code to make the deployed page more unique and appealing to users (as a terminal window on a plain white background is alienating to many people).

#### Background image

I chose a [background image](assets/images/sweet-potatoes.webp) of a colorful dish of sweet potatoes, purple onions and thyme being prepared, to illustrate the joy and labor that goes into throwing a dinner party.

#### Button design

I changed the background color of the **Run Program** button to the purple color of the onions from the background image (with the help of [ImageColorPicker](https://imagecolorpicker.com/)).
This color was chosen to harmonize with the image but still stand out from the rest of the elements on the page.

The color contrast with the white text was checked for accessibility/legibility (see [Color contrasts](#color-contrasts) for more details).


I have also made the button and the text on it larger and increased the font weight.
To balance out these changes, I also increased the button width and its margin.

Finally, I added a hover cursor effect.

#### Alignment of elements

I horizontally centered all elements on the page and added some top margin for a more pleasing look.

#### Favicon

I added a favicon showing a vector drawing of two wine glasses clinking, to symbolize the social nature of dinner parties. The color of  the graphic is a darker shade of the purple color chosen for the button.

#### Meta tags

I added some SEO meta tags to the HTML file, so that the site can be found more easily.

#### Design implementation credits

I followed the [American Pizza Order System project](https://github.com/useriasminna/american_pizza_order_system/) by [
Iasmina Pal](https://github.com/useriasminna) in implementing the changes above.

#### Rerolled design elements

I made some additional changes based on the [American Pizza Order System project](https://github.com/useriasminna/american_pizza_order_system/) that I have decided to reroll: although the modified `layout.html` file passed validation, the deployed page did not.

<details>
<summary>Click to see the details of the rerolll</summary>

In addition to some styling in the `head` element, the [American Pizza Order System project](https://github.com/useriasminna/american_pizza_order_system/)
added the following code to `@body` in `layout.html`:

```
<body>
    <main id="main-container">
        <h1>AMERICAN PIZZA ORDER SYSTEM</h1>
        @{body}
    </main>
</body>
```

I had adopted this code, and also added a [logo to the header](#logo) and [my name and a link to the GitHub repository](#author-information-and-github-link).

#### Header

I added the name of the app as an `h1` element before the Run button in the template. For its background, I used the purple color of the onions from the background image (with the help of [ImageColorPicker](https://imagecolorpicker.com/)).

The heading text color is white, so that it provides sufficient contrast with the background (see [Color contrasts](#color-contrasts) for more details).

##### Logo

I put the [image](assets/images/wine-glasses.webp) used for the favicon as a logo on each side of the header. Its design mirrors that of the box containing the header (box, border radius and shadow), but the colors are inverted.

##### Author information and GitHub link

I added my name and the link to the application's repository under the terminal window, using the colors already defined above.


![The rerolled site design](assets/readme-pics/rerolled-design.png)

Validating the resulting `html` file in itself passed without errors.

![layout.html passes validation](assets/readme-pics/html-validation-file.png)

However, running HTML validation for [the deployed site](https://dinner-party-planner-ee795b43bd35.herokuapp.com/), produced an error of there being multiple `<body>` tags.
I have deduced that the reason for this is that the Code Institute template adds a `<body>` tag as well, resulting in a duplicate.

![The deployed site did not pass HTML validation](assets/readme-pics/html-validation-error-start.png)

![The code of the deployed site that did not pass HTML validation](assets/readme-pics/html-validation-error-code.png)


Accordingly, I have rerolled the changes to `layout.html` that involved adding `html` elements, and kept the styling  to modifications in the `head`.
After this, both the modified `layout.html` file and the [the deployed site](https://dinner-party-planner-ee795b43bd35.herokuapp.com/) [passed the W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdinner-party-planner-ee795b43bd35.herokuapp.com%2F).

![The deployed site passes HTML validation](assets/readme-pics/html-validation-deployed.png)


</details>

#### Font

I changed the font used from Arial to Verdana. This font [is considered the most legible](https://www.myfonts.com/pages/fontscom-learning-fyti-using-type-tools-fonts-on-the-web#:~:text=The%20Verdana%C2%AE%20typeface%20is,small%20sizes%20(on%20screen).) of the popular web-safe fonts, especially for small screen sizes.

## Features


"start again" message at the end

functional use of colors/ASCII art

visual separation into screens

as little typing as possible

list of ingredients is

- transformed into a readable string
- alphabetized
- measurements names are shown instead of abbreviations
- singular/plural handled

flow ends when we run out of ingredients

don't rely on order of ingredients or dishes

written with scalability in mind, already planning for integrating more features (e.g. dish types)

### Not part of the MVP

#### OOP

#### Validator functions made general-purpose

#### Show input in error messages

Error message text also changes depending on function parameters (int/float), upper bound or no


#### Pantry checker

This inspired a lot of restructuring, refactoring, splitting up functions and rethinking the logic, so it had the added benefit of much cleaner and better code as a result, on top of the actual functionality (which is super relevant to real life)

list of such refactoring

pantry checker features:
- handles floats without upper bound
- measurements names are shown instead of abbreviations
- removes ingredients with quantity less than 0
- handles singular/plural

### Future features

There are several extra features and extensions planned for this project that were outside the MVP and were unrealistic to complete in the allotted time of 2 weeks.

They are viewable in [GitHub Issues](https://github.com/blahosyl/dinner-party/issues?q=is%3Aissue++is%3Aopen+label%3Aoptional), including extensive mock code for possible implementation. 

### Accessibility

#### Color contrasts

The [WebAIM](https://webaim.org/resources/contrastchecker/) was used to ensure that the text and background color of the heading provides sufficient contrast for legibility.

The colors used in the project are as follows:

|color name 	|HEX code|Comment|
|---			|---	|---|
|white			|#FFFFFF| |
|onion-purple	|#7A2F40| |
|thyme-green	|#5A5A26| Not used in the final version, but still visible in the screenshot [here](#logo).|


The paired colors have the following contrasts:

| color 1 |color 2 |contrast | [WCAG AAA](https://ialabs.ie/what-is-the-difference-between-wcag-a-aa-and-aaa/) |
|---			|---		|:---:		|:---:|
|onion-purple 	|white 	|9.09:1 	| ✅ |
|thyme-green	 	|white 	|7.17:1 	| ✅ |

## Technologies used

### Languages used

Python

### External libraries used

Which libraries are used and what their purpose is, why they are needed


### Tools used

- [Convert images to `webp` format](https://cloudconvert.com/jpeg-to-webp)
- [Pick colors from an image](https://imagecolorpicker.com/)


### Development process

tools used
GitHub Projects, Issues, branches (deleted when completed)

## Deployment

### Fork the repository

You can fork the repository by following these steps:

1. Log in to [GitHub](https://github.com/) (if you don't have a GitHub account yet, you can [create one](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github) for free).
2. Navigate to the project website [https://github.com/blahosyl/dinner-party](https://github.com/blahosyl/dinner-party).
3. Click on **Fork** in the upper right part of the screen.
4. On the next page you have the possibility to change the repository name. To do this, simply write your desired name in the text field in the center part of the screen. You can also leave the name as it is.
5. Click **Fork** in the bottom right part of the screen.

>[!TIP]
>If you do rename the repository, make sure to keep the [GitHub naming conventions](https://github.com/bcgov/BC-Policy-Framework-For-GitHub/blob/master/BC-Gov-Org-HowTo/Naming-Repos.md) in mind.

### Deployment to Heroku

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


## Testing

See the document [`TESTING.md`](TESTING.md) for details.

## Credits

### Study/lookup sources

The following resources were used to learn/double check general, atomic functionalities/syntax:

- [`gspread` user guide](https://docs.gspread.org/en/v6.0.0/user-guide.html)
- [Copy list so it can be changed without affecting the original list](https://stackoverflow.com/a/25004389)
- [Remove item from list](https://www.w3schools.com/python/python_lists_remove.asp)
- [Docstring conventions](https://peps.python.org/pep-0257/)
- [Get combinations of items from a list](https://stackoverflow.com/a/16603347)
- [`itertools` package documentation](https://docs.python.org/3/library/itertools.html#itertools.combinations)
- [Add items to list](https://www.w3schools.com/python/python_lists_add.asp)
- [Remove specified item from a list](https://www.w3schools.com/python/python_lists_remove.asp)
- [Check if a string is empty](https://stackoverflow.com/a/9573259)
- [Convert `input` to `int` with `Try/Except`](https://www.tutorialsteacher.com/articles/convert-input-to-number-in-python)
- [`try`/`except`](https://www.w3schools.com/python/python_try_except.asp)
- [Errors and exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Input validation: integer in range (did not work)](https://stackoverflow.com/questions/11594605/python-excepting-input-only-if-in-range)
- [Insert a substring before/after a certain characted in a string](https://stackoverflow.com/a/30232424/24248624)
- [Delete a character from a string](https://builtin.com/software-engineering-perspectives/python-remove-character-from-string)
- [Fix `TERM environment variable not set` error](https://stackoverflow.com/a/65161315/24248624)
- [Clear the terminal](https://www.geeksforgeeks.org/clear-screen-python/)
- [Naming conventions](https://peps.python.org/pep-0008/)
- [Naming global vs. local variables](https://stackoverflow.com/questions/69193413/why-does-the-python-style-guide-suggest-the-same-style-for-both-global-and-local)
- [Conventions for putting modules into separate files](https://stackoverflow.com/questions/2864366/are-classes-in-python-in-different-files)
- [Classes of the same module can be grouped in the same file](https://softwareengineering.stackexchange.com/a/306492)
- [Print floats in general notation - only print decimal point and decimal place digits if they are "not empty"](https://stackoverflow.com/a/2440708/24248624)
- [String operations](https://docs.python.org/3/library/string.html#format-specification-mini-language)
- [Cut off last character of string](https://stackoverflow.com/a/15478161/24248624)
- [Regular expressions for letters (not used)](https://stackoverflow.com/a/3617808/24248624)
- [`partition` method example ](https://stackoverflow.com/a/54608451/24248624)
- [`partition` method on W3Schools](https://www.w3schools.com/python/ref_string_partition.asp)
- [`colorama` documentation](https://pypi.org/project/colorama/)
- [Escape special characters in ACII art](https://code-institute-room.slack.com/archives/C027C3S3TEU/p1636456674153400?thread_ts=1636388878.151000&cid=C027C3S3TEU
)
- [String literals with `r`](https://stackoverflow.com/a/4780104/24248624)
- [Web-safe fonts](https://www.w3schools.com/cssref/css_websafe_fonts.php)
- [Verdana properties](https://www.myfonts.com/pages/fontscom-learning-fyti-using-type-tools-fonts-on-the-web#:~:text=The%20Verdana%C2%AE%20typeface%20is,small%20sizes%20(on%20screen).)
- [not capitalizing "daiquiri"](https://www.latimes.com/socal/daily-pilot/opinion/tn-hbi-et-1231-casagrande-20151231-story.html)
- [not capitalizin "bloody mary"](https://www.latimes.com/socal/daily-pilot/opinion/story/2020-08-04/a-word-please-lowercase-treatment-in-newswriting-can-humble-important-words#:~:text=But%20since%20the%20drink%20was,drink%20names%20are%20more%20flexible.)
- [`pyfiglet` usage](https://medium.com/@parcelmaiyo/text-styling-in-python-using-pyfiglet-824c498dfff5)
- [sort list of lists](https://stackoverflow.com/a/54116034/24248624)
- [problems with removing list items in a loop and some solutions (not used)](https://stackoverflow.com/a/6260097/24248624)
- [fix list comprehension error with indices (not used)](https://codinggear.org/list-indices-must-be-integers-or-slices-not-list/#:~:text=The%20Python%20Typeerror%3A%20list%20indices,index%20instead%20of%20a%20list.)
- [`isnumeric`: only allow numeric values](https://stackoverflow.com/a/72488576/24248624)
- [infinity](https://www.geeksforgeeks.org/python-infinity/)
- [defining functions with optional arguments](https://realpython.com/python-optional-arguments/)

### Code credits

The following sources contributed code or suggestions to specific functions within the project:

Rory Patrick Sheridan, my mentor, gave suggestions, helped me solve or spotted bugs described in [these Issues](https://github.com/blahosyl/dinner-party/issues?q=is%3Aissue+label%3Amentor) (see the Issue descriptions and comments for details).

Modifying the `layout.html` file in the Code Institute template to change some CSS styling was done following but also revising the method used in the [American Pizza Order System project](https://github.com/useriasminna/american_pizza_order_system/) by [
Iasmina Pal](https://github.com/useriasminna) (see the section [Rerolled design elements](#rerolled-design-elements) for details).

@nobe4 and [Zerina Johansson](https://code-institute-room.slack.com/archives/C01DVU37QG4/p1713290110344539) helped me solve the issue of [printing out the user input in a `try/except` loop](https://github.com/blahosyl/dinner-party/commit/bed421e4bbbe1400df09fcfde4d71438d585d7b1).

@nobe4 also gave me valuable advice on organizing code, and helped me solve the [bug in displaying the correct user input in a `try/except` block](https://github.com/blahosyl/dinner-party/issues/41).

Finally, I would like to thank an enthusiastic apha tester who wished to remain anonymous.


### Content

All text content was written by me.

### Media

#### Images

[Background image](assets/images/sweet-potatoes.webp) by me, coverted to `webp` with [CloudConvert]((https://cloudconvert.com/jpeg-to-webp)
).

[Image](assets/images/wine-glasses.webp) for the favicon and logo from [Vecteezy](https://www.vecteezy.com/vector-art/2602820-wine-cups-glasses-toasting-line-style-icon), converted to `png` format with Preview, converted to `ico` format with [Favicon.io](https://favicon.io/), coverted to `webp` with [CloudConvert](https://cloudconvert.com/jpeg-to-webp).

### Readme

- [Creating your first README with Kera Cudmore](https://www.youtube.com/watch?v=XbYJ4VlhSnY) by Code Institute
- [Creating your first README](https://github.com/kera-cudmore/readme-examples) by Kera Cudmore
- [Bully Book Club](https://github.com/kera-cudmore/Bully-Book-Club) by Kera Cudmore
- [Bodelschwingher Hof](https://github.com/4n4ru/CI_MS1_BodelschwingherHof/tree/master) by Ana Runje
- [Travel World](https://github.com/PedroCristo/portfolio_project_1/) by Pedro Cristo
- [Sourdough Bakes](https://github.com/siobhanlgorman) by Siobhan Gorman
- [Horizon Photo](https://github.com/Ri-Dearg/horizon-photo/blob/master/README.md#mobile-testing) by Rory Patrick Sheridan
- [The README of my first Code Institute project](https://github.com/blahosyl/academic-publishing)
- [The README of my second Code Institute project](https://github.com/blahosyl/operator-game)
