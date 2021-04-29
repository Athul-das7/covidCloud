import prototypeRasp as p
import prototypeCloud as pc
import time
import gspread
from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import numpy as np

test = p.covidCloud()
test1 = pc.cloudPrediction()
rnum = test.readBarcode()
print(rnum)
test.checkRollNo(rnum)
time.sleep(3)
ckdis = False
dist = 2.00
temp=0
while ckdis!=True:
    dist = test.readDistance()
    print(dist, " cm")
    ckdis = test.checkDistance(dist)
    if ckdis == True:
        temp=test.readTemperature()
    else:
        print(" please put your hand closer to the sensor")
        time.sleep(2)
        continue

print(temp)
test1.predict()