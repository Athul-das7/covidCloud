import prototypeRasp as p

test = p.covidCloud()
print(test.checkTemperature(92))
temp = test.readTemperature()
rn = test.readBarcode()
print(rn,temp)
#test.sendMail(rn,temp)

print(a)
