import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time

# use creds to create a client to interact with the Google Drive API
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

#scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("testing").sheet1

# Extract and print all of the values
list_of_hashes = sheet.get_all_records()
print(list_of_hashes)

val = sheet.get_all_values()
print(val)
val = sheet.row_values(1)
print(val)
val = sheet.col_values(1)
print(val)
val = sheet.cell(1, 1).value
print(val)
for i in range(1,1024):
    val = sheet.update_cell(i, 13, i)
    print(val)
    time.sleep(30)
print(val)
row = ["I'm","inserting","a","row","into","a,","Spreadsheet","with","Python"]
index = 4
val = sheet.insert_row(row, index)

print(val)
val = sheet.col_count
print(val)