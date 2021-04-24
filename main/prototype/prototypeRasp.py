# this code goes into Raspberry pi 

# test the functionality of you code in athul.py or mounika.py file
# replace the pass and add your function
# use the existing code in the test directory as you see fit from anyones folder and complete the function

'''Import all the necessary libraries as you see fit '''
import random
import time
import winsound
import smtplib as sl      #import the smtp library to send mail through scripts
import requests   #importing the requests library to send html requests
import json

class covidCloud:
    def readBarcode(self):
        # reads the barcode and returns the data generated
        # for now generated the roll no. using random function in string format
        rnum = str(random.randint(1, 120)).zfill(3)
        rnum = "1602-" + str(random.randint(17, 20)) + "-" + str(random.randint(732, 737)) + "-" + rnum
        return rnum
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
        return d

    def checkDistance( self, distance ):
        # checks the distance and returns true or false as per the data given
        if 2 <= distance <= 6:
            return True
        else: return False

    def readTemperature(self):
        # reads the temperature using the temperature sensor returns it
        t = round(97 + (102-97)*random.random(),3)
        return t
            # self.checkTemperature(t)

    def checkTemperature( self, temperature ):
        # check the temperature and return true or false as per the condition
        if ( temperature < 100 and temperature > 94 ):
            return True
        else :
            return False

    def Alarm(self):
        # if the function is invoked the alarm must go off for set amout of time
        for i in range(5):
            duration = 1000  # milliseconds
            freq = 5040  # Hz
            winsound.Beep(freq, duration)
            time.sleep(0.5)

    def sendMail(self, rnum,temperature):
        # send mail to the management when invoked
        smtpobj = sl.SMTP('smtp.gmail.com', 587)
        # creating a smtp object and connecting to the domain server of mail.outlook.com over the port 587

        # you can remove the print statements from the code, its placed to know the status of code execution

        smtpobj.ehlo()  # this establishes the connection with the server
        smtpobj.starttls()  # this start the ttls encryption in the server
        pswd = 'athulmounika'  # Taking the password as input is safer because if you save it in a script anyone who can access the script will be able to find the password
        smtpobj.login('covidCloudmp@gmail.com', pswd)  # login in to the smtp server

        SUBJECT = '{} temperature above 100'.format(rnum)  # subject line

        TEXT = '''Dear management,        

        Student {} is having a temperature of {}
        please take an immediate attention on this issue.

        Thank you
        '''.format(rnum,temperature)  # body of the mail

        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)  # concating the strings using string formatting

        smtpobj.sendmail('covidCloudmp@gmail.com', '1602-19-735-091@vce.ac.in', message)
        # sending the mail from us to the reciever; 071 = user; 091 = reciever; message = subject + body

        smtpobj.quit()  # quiting the smtp server and deleting the object

    def sendSMS(self, rn, temp):
        # send SMS to the management when invoked
        url = "https://www.fast2sms.com/dev/bulk"  # Using the fast2sms url
        # Create a account in fast2sms with your phone number and copy the headers creditinals
        # Now change the payload to the way you want to send the message.

        # payload = "sender_id=FSTSMS&message=Hey%20Athul&language=english&route=p&numbers=9866989137"

        # create a dictionary
        my_data = {
            # Your default Sender ID
            'sender_id': 'FSTSMS',

            # Put your message here!
            'message': '''The student {} is having temperature above {} degree farenheit.
Please come to the gate immediately'''.format(rn,temp),

            'language': 'english',
            'route': 'p',

            # You can send sms to multiple numbers
            # separated by comma.
            'numbers': '9866989137,9605861454',
        }

        headers = {
            'authorization': "q1vSrCUh2nGIAWcasdyeTuKBZ8jmbgkMLoN5pf69J0wP7Xi4ztKb86rVPnhaqBEcuYtG0UXDoZ2p1gw4",
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",

        }  # authorization credentials

        response = requests.request("POST", url, data=my_data, headers=headers)
        # Sending the response to to the url.
        # print(response.text)
        # load json data from source

        returned_msg = json.loads(response.text)

        # print the send message
        print(returned_msg['message'])

    def sendArrangeData(self,studentData):
        # send the data to google spread sheets and arrange it accordingly
        pass

# the dbms and gui can be added later to this class...or we can make use of another class for gui...
