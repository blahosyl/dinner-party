# connect to the database in Google Sheets
# and retrieve data
# code based on the Love Sandwiches project

# import entire library
import gspread
# import 1 class from a library
from google.oauth2.service_account import Credentials

# constant specifying what the Robot user has access to
SCOPE = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive'
]

# specify credentials
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# specify the name of the Google Sheets document
SHEET = GSPREAD_CLIENT.open('ingredients')

# select the worksheet in the Google Sheets document
recipes = SHEET.worksheet('main')
