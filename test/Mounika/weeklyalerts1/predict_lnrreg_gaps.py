import gspread
from df2gspread import df2gspread as d2g
import os
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
from sklearn.linear_model import LinearRegression
import time


#runs the prediction on the given data // and updates in the predict column
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("credsgss.json",
                                                         scope)  # creds is a json file which store Api keys for google sheet

client = gspread.authorize(creds)

sheet = client.open(
    "testing").sheet1  # parameter given is google sheet name "covidcloud" which stores data
data = sheet.get_all_records()
# print(data)
df = pd.DataFrame(data)
print(df)
shape = df.shape
# print(shape[1])  # returns no. of columns in the 1st row are filled


# df1 = df.columns
# print(df1)

row = len(df)    # to get no. of rows are filled
clm = len(df.columns)  # to get no. of columns are filled
print(row)
print(clm)
a = int((clm - 1)/2)    # to get no. of columns with temperature values
print(a)
file1 = open("predict_temp.txt", "w")
file1.write("roll no           --     tempetature\n")
count = 0

x = np.array(range(1, a + 1)).reshape(-1, 1)
# print(x)
# print(df.iloc[0])
# print(df.iloc[0].to_numpy()[1:])
# for j in range(1,clm,2):
#     print(df.iloc[0,j])        # printing temperature values of a row where j is column index
for i in range(row):
    sum=0.0
    n=0
    y=np.array([])
    for j in range(1,clm,2):
        tp=df.iloc[i,j]
        if tp!='':
            sum=sum+float(tp)
            n=n+1
        else:                          # i am taking average by assuming 1st day the person is not absent,i.e, 1st column of any row is not empty
            df.iloc[i,j]=str(round(float(sum/n),3))
            sum=sum+float(df.iloc[i,j])
        y=np.append(y, float(df.iloc[i,j]))
    # print(y)
    f = 0
    ls = [df.iloc[i,0], '--']
    # print(ls)
    model = LinearRegression().fit(x, y)
    y_pred = model.intercept_ + model.coef_ * (a+4)    # direct 4th day
    # print(y_pred)
    # df.at[i, p] = y_pred[0]
    ls.append(round(y_pred[0], 3))
    if (y_pred[0] > 100.4):
        f = 1
    if (f == 1):
        file1.write("   ".join([str(s) for s in ls]))
        file1.write("\n")
        count = count + 1

current_time = time.ctime()
print(df)
file1.close()
# print(current_time)
logfile = open("log.txt", "a")
logfile.write("{}   {}\n".format(current_time, count))
logfile.close()


# --------------------------------------------------------------------------------------------------------
# previous predict using circular regression
# let this be here

#runs the prediction on the given data // and updates in the predict column
# scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
#          "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
#
# creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",
#                                                          scope)  # creds is a json file which store Api keys for google sheet
#
# client = gspread.authorize(creds)
#
# sheet = client.open(
#     "Temperature report").sheet1  # parameter given is google sheet name "covidcloud" which stores data
# data = sheet.get_all_records()
# # print(data)
# df = pd.DataFrame(data)
# print(df)
# shape = df.shape
# print(shape[1])  # returns no. of columns in the 1st row are filled
# no_c = shape[1] - 2
#
# df1 = df.columns
# print(df1)
# df1 = df['1']
# print(df1)
# row = len(df)
# clm = len(df.columns)
# a = clm - 2
#
# file1 = open("predict_temp.txt", "w")
# file1.write("roll no           --     1         2         3          4\n")
# count = 0
# for i in range(len(df)):
#     x = np.array(range(1, a + 1)).reshape(-1, 1)
#     sub = df.iloc[i].to_numpy()[2:a + 2]    # to retrive row values from dataframe
#     f = 0
#     ls = [df.at[i, 'roll no'], '--']
#     print(ls)
#     for j in range(a + 1, a + 5):
#         model = LinearRegression().fit(x, sub)
#         p = '{}'.format(j)
#         # print(p)
#         y_pred = model.intercept_ + model.coef_ * j
#         # print(y_pred)
#         df.at[i, p] = y_pred[0]
#         ls.append(round(y_pred[0], 3))
#         if (y_pred[0] > 100.4):
#             f = 1
#
#         x = np.array(range(1, j + 1)).reshape(-1, 1)
#         sub = df.iloc[i].to_numpy()[2:j + 2]
#         # print(sub)
#         # print(x)
#     if (f == 1):
#         file1.write("   ".join([str(s) for s in ls]))
#         file1.write("\n")
#         count = count + 1
#
# current_time = time.ctime()
# # print(df)
# file1.close()
# # print(current_time)
# logfile = open("log.txt", "a")
# logfile.write("{}   {}\n".format(current_time, count))
# logfile.close()
#
#
#
#
#
