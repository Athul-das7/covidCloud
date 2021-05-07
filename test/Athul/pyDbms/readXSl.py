#Reads the excel and creates a database type script
import pandas as pd

sheet = pd.read_excel('data.xlsx')
#sheet.drop(index='Name of the College: Vasavi College of Engineering (Autonomous)')

f = open('sql.txt','a')   #this is the normal one

#print(sheet)
b = 'gotchya'
for i in range(len(sheet)):
    num = sheet.iloc[i,0]
    #print(type(rn))
    rn = num
    nm = sheet.iloc[i,2]

    #print(rn)
    if rn == 1 :
        b = 'A'
    elif rn is 61 :
        b = 'B'
    elif rn is 121 :
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
#with open('sql.txt','a') as f:    #this with open
    #f.write(f'("1602-19-735-{rn}","{nm}","ECE","{b}","media\\\\{num}.jpg"),\n')