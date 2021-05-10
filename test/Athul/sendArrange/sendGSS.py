import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date
import time


'''Connect to the spread sheet'''
# use creds to create a client to interact with the Google Drive API
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

#scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("testing").sheet1


today = date.today()
today = today.strftime("%Y/%m/%d")
#print(type(today))


FirstCell = sheet.cell(1,1).value #first cell contains the max row and max column number
#print(FirstCell)
mrow,mcol = FirstCell.split(':')
mrow = int(mrow)    #max row count
mcol = int(mcol)    #max column count


try:
    todCol = sheet.find(today).col      #column for today
    #print(todCol)
except:
    sheet.update_cell(1,mcol,today)
    todCol = mcol       #column for today
    mcol += 1
    sheet.update_cell(1,1,f'{mrow}:{mcol}')     #update the cell in (1,1) to new value
    #print(mcol)

f = open('TempRoll.txt','r')
data = f.read()
f.close()
f = open('TempRoll.txt','w')
f.close()
data = data.split('\n')
print(data)
#i = input()

past = time.time()
now = time.time()
for i in data:
    if i == '':
        continue
    now = time.time()
    rollno = i.split(':')[0]
    temp = i.split(':')[-1]
    try :
        todRow = sheet.find(rollno).row     #Row corresponding to roll no. of student
        #print(todRow)
    except :
        todRow = mrow                   #Row corresponding to roll no. of student
        sheet.update_cell(mrow,1,rollno)
        mrow += 1
        sheet.update_cell(1, 1, f'{mrow}:{mcol}')  #updating the cell (1,1) to the new values
        #print(mrow)

    if now - past > 15:
        #print('Sleep for 40secs')
        time.sleep(40)
        past = time.time()
        now = time.time()
    val = sheet.update_cell(todRow,todCol,temp)


'''1602-19-735-001: 97
1602-19-735-071: 91
1602-19-735-072: 92
1602-19-735-073: 93
1602-19-735-074: 93
1602-19-735-075: 94
1602-19-735-076: 95
1602-19-735-171: 96
1602-19-735-172: 97
1602-19-735-173: 97
1602-19-735-174: 98
1602-19-735-175: 99
1602-19-735-176: 90
1602-19-735-051: 91
1602-19-735-052: 92
1602-19-735-053: 23
1602-19-735-054: 983
1602-19-735-055: 985
1602-19-735-056: 986
'''

#for every 30mins I will run this thread and let it finish when it finishes when text file is not empty