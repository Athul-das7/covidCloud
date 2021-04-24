import prototypeRasp as p
import time

test = p.covidCloud()
rnum = test.readBarcode()
print(rnum)
test.checkRollNo(rnum)
time.sleep(3)
ckdis = False
dist = 2.00
while ckdis!=True:
    dist = test.readDistance()
    print(dist, " cm")
    ckdis = test.checkDistance(dist)
    if ckdis == True:
        print(test.readTemperature())
    else:
        print(" please put your hand closer to the sensor")
        time.sleep(2)
        continue


