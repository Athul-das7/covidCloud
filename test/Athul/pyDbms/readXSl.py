#Reads the excel and creates a database type script
import pandas as pd

sheet = pd.read_excel('ISF_ECE_Vasavi_Hyd_2018-19.xlsx')
#sheet.drop(index='Name of the College: Vasavi College of Engineering (Autonomous)')

f = open('sql.txt','a')   #this is the normal one
for i in sheet:
    print(i)
    #    print(j)
print(sheet)
b = 'gotchya'
for i in range(len(sheet)):
    num = sheet.iloc[i,0]
    rn = num
    #print(type(rn)
    nm = sheet.iloc[i,2]

    #print(rn)
    if rn == 1 :
        b = 'A'
    elif rn == 61 :
        b = 'B'
    elif rn == 121 :
        b = 'C'
    #print(b)
    if isinstance(rn,int):
        if rn//10 == 0:
            rn = str(rn)
            rn = '00'+str(rn)
        elif rn//100 == 0:
            rn = str(rn)
            rn = '0' + str(rn)
    if isinstance(nm,str):
        if len(nm) > 30:
            print(rn)
    with open('sql.txt','a') as f:    #this with open
        f.write(f'("1602-18-735-{rn}","{nm}","ECE","{b}","media\\\\18\\\\{num}.jpg"),\n')