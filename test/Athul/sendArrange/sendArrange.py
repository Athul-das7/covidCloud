import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date
import time

today = date.today()
print("Today's date:", today.strftime("%d/%m/%Y"))
d1 = today.strftime("%d/%m/%Y")

# use creds to create a client to interact with the Google Drive API
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

#scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("testing").sheet1

FirstCell = sheet.cell(1, 1).value  # first cell contains the max row and max column number
# print(FirstCell)
mrow, mcol = FirstCell.split(':')
mrow = int(mrow)  # max row count
mcol = int(mcol)  # max column count

# Extract and print all of the values
#list_of_hashes = sheet.get_all_records()
#print(list_of_hashes)

if mcol == 31:
    val = sheet.batch_get(['C:AE'])
    #sheet.delete_columns(31,60)
    #sheet.add_cols(2)
    print(val)
    for i in val:
        print(i)
        '''sheet.batch_update([{
            'range': 'B:AD',
            'values': i,
        }])'''
        sheet.update('B:AD',i)
    sheet.update_cell(1,1,f'{mrow}:{mcol-1}')