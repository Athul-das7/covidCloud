#All the code required to fuction in cloud must be written here...

#test the functionality of your code in athul.py or mounika.py file
#replace pass and add your function
#use the existing code in the test directory as you see fit from anyones folder and complete the function

''' Import all the necessary libraries as you see fit '''
import smtplib as sl      #import the smtp library to send mail through scripts
import requests   #importing the requests library to send html requests
import json

class cloudPrediction:
    def readDataSheets(self):
        #reads data from the google spread sheets and returns it
        pass
    def predict(self,studentData):
        #runs the prediction on the given data 
        pass
    def sendMail(self,rnum,temperature,flag):
        #sends mail to all if flag is false else sends mail to the student and the management 
        # send mail to the management when invoked
        smtpobj = sl.SMTP('smtp.gmail.com', 587)
        # creating a smtp object and connecting to the domain server of mail.outlook.com over the port 587

        # you can remove the print statements from the code, its placed to know the status of code execution

        smtpobj.ehlo()  # this establishes the connection with the server
        smtpobj.starttls()  # this start the ttls encryption in the server
        pswd = 'athulmounika'  # Taking the password as input is safer because if you save it in a script anyone who can access the script will be able to find the password
        smtpobj.login('covidCloudmp@gmail.com', pswd)  # login in to the smtp server

        if flag:
            SUBJECT = '{} temperature above 100'.format(rnum)  # subject line

            TEXT = '''Dear management,        
    
            Student {} is having a predicted temperature of {}
            Please take immediate attention over this issue.
    
            Thank you
            '''.format(rnum, temperature)  # body of the mail
        else :
            SUBJECT = '{} weekend report'.format(rnum)  # subject line

            TEXT = '''Dear {},
            Your weekend temperature report is {}.
                        
            Thank you'''.format(rnum, temperature)  # body of the mail

        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)  # concating the strings using string formatting

        smtpobj.sendmail('covidCloudmp@gmail.com', '1602-19-735-071@vce.ac.in', message)
        # sending the mail from us to the reciever; 071 = user; 091 = reciever; message = subject + body

        smtpobj.quit()  # quiting the smtp server and deleting the object

    def sendSMS(self,rn,temp,flag):
        #sends sms to management if flag is true
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
            'message': '''The student {} is having predicted temperature above {} degree farenheit.
Please take caution'''.format(rn, temp),

            'language': 'english',
            'route': 'p',

            # You can send sms to multiple numbers
            # separated by comma.
            'numbers': '9866989137',
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


#dbms to be thought later
