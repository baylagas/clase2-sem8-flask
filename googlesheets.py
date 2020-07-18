import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]


creds = ServiceAccountCredentials.from_json_keyfile_name(
    "clase-esen-test-6350d15efb04.json", scope
)

client = gspread.authorize(creds)

sheet = client.open("bal-esen-sheet").worksheet("alumnos")
