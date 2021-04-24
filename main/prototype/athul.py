import prototypeRasp as p

test = p.covidCloud()
print(test.checkTemperature(92))
temp = test.readTemperature()
rn = test.readBarcode()
#test.sendMail(rn,temp)
s='athul'
d='das'
a = '{} and {} '.format(s,d)
print(a)
