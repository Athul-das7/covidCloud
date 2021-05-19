import prototypeRasp as p
import prototypeCloud as pp

#test = pp.cloudPrediction() #p.covidCloud()
test = p.covidCloud()
#test.readDistance()
#test.readTemperature()
rn = test.readBarcode()
test.checkRollNo(rn)
#test.alterSpreadSheet();

'''temp = 97.0
rn = '1602-19-735-064'
print(rn,temp)
#print(test.readDbms(rn))

test.sendMail(rn,temp)'''