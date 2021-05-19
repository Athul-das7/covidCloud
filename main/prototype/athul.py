import prototypeRasp as p
import prototypeCloud as pp

test = pp.cloudPrediction() #p.covidCloud()
#test = p.covidCloud()
test.sendMail()
#test.alterSpreadSheet();

'''temp = 97.0
rn = '1602-19-735-064'
print(rn,temp)
#print(test.readDbms(rn))

test.sendMail(rn,temp)'''