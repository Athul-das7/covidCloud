# this code goes into Raspberry pi 

#test the functionality of you code in athul.py or mounika.py file
#replace the pass and add your function
#use the existing code in the test directory as you see fit from anyones folder and complete the function

''' Import all the necessary libraries as you see fit '''

class covidCloud:
    def readBarcode(self):
        #reads the barcode and returns the data generated 
        pass
    def checkRollNo( self, barcode ):
        #checks the data recived from barcode scanner and returns true or false
        pass
    def readDistance(self):
        #reads the distance using ultrasonic sensor and returns it
        pass
    def checkDistance( self, distance ):
        #checks the distance and returns true or false as per the data given
        pass
    def readTemperature(self):
        #reads the temperature using the temperature sensor returns it
        pass
    def checkTemperature( self, temperature ):
        #check the temperature and return true or false as per the condition
        pass
    def Alarm(self):
        #if the function is invoked the alarm must go off for set amout of time
        pass
    def sendMail(self, studentData):
        #send mail to the management when invoked 
        pass
    def sendSMS(self, studentData):
        #send SMS to the management when invoked 
        pass
    def sendArrangeData(self,studentData):
        #send the data to google spread sheets and arrange it accordingly
        pass

#the dbms and gui can be added later to this class...or we can make use of another class for gui...
