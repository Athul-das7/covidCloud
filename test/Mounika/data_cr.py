import gspread
from df2gspread import df2gspread as d2g
import os
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


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


df1=df.columns
print(df1)
df1=df['1']
print(df1)
# df['1']=df['2']
# print(df)
row=len(df)
clm=len(df.columns)
a=clm-2

# df1 = pd.DataFrame({a+1:[],
#                     a+2:[],
#                     a+3:[],
#                     'a+4':[]
#                     })
# df = df.append(df1, ignore_index = True)
# print(df1)
# print(df)

file1 = open("predict_temp.txt","w")
file1.write("roll no           --     1         2         3          4\n")
for i in range(len(df)):
    x = np.array(range(1, a + 1)).reshape(-1, 1)
    # print(type(df.iloc[i].values))
    # print(df.iloc[i].to_numpy())
    sub=df.iloc[i].to_numpy()[2:a+2]
    # print(type(sub))
    f=0
    ls=[df.at[i, 'roll no'],'--']
    print(ls)
    # file1.write("".join([str(x) for x in ls]))
    for j in range(a + 1, a + 5):
        model = LinearRegression().fit(x, sub)
        # y_pred = model.predict(j)
        p = '{}'.format(j)
        # print(p)
        y_pred = model.intercept_ + model.coef_ * j
        # print(y_pred)
        df.at[i, p] = y_pred[0]
        ls.append(round(y_pred[0],3))
        if(y_pred[0]>100.4):
            f=1
        x = np.array(range(1, j + 1)).reshape(-1, 1)
        sub = df.iloc[i].to_numpy()[2:j + 2]
        # print(sub)
        # print(x)
    if(f==1):
          file1.write("   ".join([str(s) for s in ls]))
          file1.write("\n")

print(df)
file1.close()

print(df['11'])