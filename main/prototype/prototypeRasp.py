# this code goes into Raspberry pi 

# test the functionality of you code in athul.py or mounika.py file
# replace the pass and add your function
# use the existing code in the test directory as you see fit from anyones folder and complete the function

'''Import all the necessary libraries as you see fit '''
import random

class covidCloud:
    def readBarcode(self):
        # reads the barcode and returns the data generated
        # for now generated the roll no. using random function in string format
        rnum = str(random.randint(1, 120)).zfill(3)
        rnum = "1602-" + str(random.randint(17, 20)) + "-" + str(random.randint(732, 737)) + "-" + rnum
        print(rnum)
        self.checkRollNo(rnum)
    # def checkRollNo( self, barcode ):
    def checkRollNo(self, rnum):
        # checks the data recived from barcode scanner and returns true or false
        # received form function readBarcode()
        num = rnum.split('-')
        f=True
        if int(num[0]) != 1602: f = False
        elif int(num[1]) not in range(17, 21) == True:
            f = False
        elif int(num[2]) not in range(732, 738) == True:
            f = False
        elif int(num[3]) not in range(1, 121) == True:
            f = False
        if f == True:
            print("Valid")
            print("please put your hand near temperature sensor")
        else:
            print("INvalid Id")

    def readDistance(self):
        # reads the distance using ultrasonic sensor and returns it
        # for now generating random distance
        d = round(2 + (6)*random.random())     # min + (max-min)*random.random()  , here  generates in range 2-8
        if self.checkDistance(d):
            return True
        else:
            print(" please put your hand closer to the sensor")
            if self.readDistance():
                return True

    def checkDistance( self, distance ):
        # checks the distance and returns true or false as per the data given
        if 2 <= distance <= 6:
            return True
        else: return False

    def readTemperature(self):
        # reads the temperature using the temperature sensor returns it
        if self.readDistance() == True:
            t = round(97 + (102-97)*random.random(),3)
            print(t)
            # self.checkTemperature(t)

    def checkTemperature( self, temperature ):
        # check the temperature and return true or false as per the condition
        pass
    def Alarm(self):
        # if the function is invoked the alarm must go off for set amout of time
        pass
    def sendMail(self, studentData):
        # send mail to the management when invoked
        pass
    def sendSMS(self, studentData):
        # send SMS to the management when invoked
        pass
    def sendArrangeData(self,studentData):
        # send the data to google spread sheets and arrange it accordingly
        pass

# the dbms and gui can be added later to this class...or we can make use of another class for gui...
