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
no_c = shape[1]-2

l = len(data)
c = chr(ord('C')+no_c)      # next day column letter
cur_c = chr(ord('C')+no_c-1)
print(c)
r = 2
print("=forecast({}1, C{}:{}{}, C1:{}1)".format(c, r, cur_c, r, cur_c))

# for r in range(2,l+2):
#     # row=sheet.row_values(r)
#     # print(row)
#     sheet.update_cell(1, shape[1]+1, no_c+1)
#     sheet.update_cell(r, 2, "=forecast({}1, C{}:{}{}, C1:{}1)".format(c, r, cur_c, r, cur_c))
    # time.sleep(30)
# we won't be doing this forecast until we collect 1 week of data
# the above for loop is for 1st two weeks data update

# mask = ~(df.columns.isin(['roll no', 'predict']))
# print(mask)
# rows_to_shift = df.columns[mask]
# print(rows_to_shift)
#
# df[rows_to_shift] = df.loc[:,mask].shift(-1)
# print(df[rows_to_shift])
df1=df.columns
print(df1)
df1=df['1']
print(df1)
df['1']=df['2']
print(df)
# existing = pd.DataFrame(df.get_all_records())
# df.drop(columns=[' '],axis=1,inplace=True)
# print(df)
# d2g.upload(df, spreadsheet_key, credentials=creds, row_names=True)



        # data = sheet.get_all_records()
        # spreadsheet_key = '1lzg0ZKb_EnJ_s5FVRSD8zEbYCVtLwWMIf_fDMQhWisM'
        # df = pd.DataFrame(data)
        # print(df)     # prints the whole data retrived from the sheet -> remove this-> just for checking
        # shape = df.shape
        # print(shape[1])  # returns no. of columns in the 1st row are filled
        # no_c = shape[1] - 2   # no. of days data is taken-> Column C to till where it is filled
        # l = len(data)   # for no. of rows
        # c = chr(ord('C') + no_c)  # next day column letter
        # cur_c = chr(ord('C') + no_c - 1)
        # # print(c)
        # for r in range(2,l+2):
        #     # row=sheet.row_values(r)
        #     # print(row)
        #     sheet.update_cell(1, shape[1]+1, no_c+1)
        #     sheet.update_cell(r, 2, "=FORECAST({}1, C{}:{}{}, C1:{}1)".format(c, r, cur_c, r, cur_c))'''






