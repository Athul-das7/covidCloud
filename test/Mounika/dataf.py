import gspread
from df2gspread import df2gspread as d2g
import os
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)   #creds is a json file which store Api keys for google sheet

client = gspread.authorize(creds)

sheet = client.open("Temperature report").sheet1   #parameter given is google sheet name "covidcloud" which stores data
data = sheet.get_all_records()
spreadsheet_key = '1lzg0ZKb_EnJ_s5FVRSD8zEbYCVtLwWMIf_fDMQhWisM'

# print(data)
df = pd.DataFrame(data)
print(df)
shape = df.shape
print(shape[1])      # returns no. of columns in the 1st row are filled
'''no_c = shape[1]-2

l = len(data)
c = chr(ord('C')+no_c)      # next day column letter
cur_c = chr(ord('C')+no_c-1)
print(c)
r = 2
print("=forecast({}1, C{}:{}{}, C1:{}1)".format(c, r, cur_c, r, cur_c))
'''
df1 = pd.DataFrame({"10":[1, 2, 3, 4],
                    "11":[5, 6, 7, 8],
                    "12":[5, 6, 7, 8],
                    "13":[5, 6, 7, 8]
                    })
df = df.append(df1, ignore_index = True)
print(df)
rollno = 147397
temp = 99
with open('log.txt','a') as fh:
    fh.write(f'{rollno} {temp}\n')