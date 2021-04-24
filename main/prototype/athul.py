import prototypeCloud as p

test = p.cloudPrediction()

temp = 97
rn = '1602-19-735-000'
print(rn,temp)
test.sendMail(rn,temp,False)


