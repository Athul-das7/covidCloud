# install libraries
#pip install gspread oauth2client
#pip install google-api-python-client
#pip install google-auth-httplib2
#pip install google-auth-oauthlib

import mailalert1        # imported python file which sends mail to each member
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)   #creds is a json file which store Api keys for google sheet

client = gspread.authorize(creds)

sheet = client.open("covidcloud").sheet1   #parameter given is google sheet name "covidcloud" which stores data
data = sheet.get_all_records()
#print(data)
l=len(data)            #gets the no.of rows which are filled -1
#print(l)
#row = sheet.row_values(2)
#print(row)
#print(type(row))
#print(row[1])
for r in range(2,l+2):
    row=sheet.row_values(r)
    mailalert1.send_alert(row)   #calling function send_alert() for each user imported form another file
    #print(row)

# must create another google account and get API keys for that account and store in Creds.json file
#creds.json  file is not written , but gets downloaded itself into the specified directory while generating API key for goole sheet
