#All the code required to fuction in cloud must be written here...

#test the functionality of your code in athul.py or mounika.py file
#replace pass and add your function
#use the existing code in the test directory as you see fit from anyones folder and complete the function

''' Import all the necessary libraries as you see fit '''
import smtplib as sl      #import the smtp library to send mail through scripts
import requests   #importing the requests library to send html requests
import json
import gspread
#from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import numpy as np
from multipledispatch import dispatch    # for method overloading
from datetime import date
from sklearn.linear_model import LinearRegression
import time

class cloudPrediction:
    def readDataSheets(self):
        #reads data from the google spread sheets and returns it
        pass

    def alterSpreadSheet(self):
        # use creds to create a client to interact with the Google Drive API
        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                 "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

        # scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name('credsgss.json', scope)
        client = gspread.authorize(creds)

        # Find a workbook by name and open the first sheet
        # Make sure you use the right name here.
        sheet = client.open("testing").sheet1

        FirstCell = sheet.cell(1, 1).value  # first cell contains the max row and max column number
        # print(FirstCell)
        mrow, mcol = FirstCell.split(':')
        mrow = int(mrow)  # max row count
        mcol = int(mcol)  # max column count


        if mcol == 60:
            val = sheet.batch_get(['D:BD'])     #get batch data of the spread sheet
            # sheet.delete_columns(31,60)
            # sheet.add_cols(2)
            print(val)
            for i in val:
                print(i)
                sheet.update('B:BB', i)   #update and change the spread sheet
            sheet.update_cell(1, 1, f'{mrow}:{mcol - 2}')

    # def predict(self,studentData):    # as per student data will be checked later
    def predict(self):                   # this will run only once from main
        # runs the prediction on the given data // and updates in the predict column
        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                 "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("credsgss.json",
                                                                 scope)  # creds is a json file which store Api keys for google sheet

        client = gspread.authorize(creds)

        sheet = client.open(
            "testing").sheet1  # parameter given is google sheet name "covidcloud" which stores data
        data = sheet.get_all_records()
        # print(data)
        df = pd.DataFrame(data)
        print(df)
        shape = df.shape
        # print(shape[1])  # returns no. of columns in the 1st row are filled

        # df1 = df.columns
        # print(df1)

        row = len(df)  # to get no. of rows are filled
        clm = len(df.columns)  # to get no. of columns are filled
        print(row)
        print(clm)
        a = int((clm - 1) / 2)  # to get no. of columns with temperature values
        print(a)
        file1 = open("predict_temp.txt", "w")
        file1.write("roll no           --     tempetature\n")
        count = 0

        x = np.array(range(1, a + 1)).reshape(-1, 1)
        # print(x)
        # print(df.iloc[0])
        # print(df.iloc[0].to_numpy()[1:])
        # for j in range(1,clm,2):
        #     print(df.iloc[0,j])        # printing temperature values of a row where j is column index
        for i in range(row):
            sum = 0.0
            n = 0
            y = np.array([])
            for j in range(1, clm, 2):
                tp = df.iloc[i, j]
                if tp != '':
                    sum = sum + float(tp)
                    n = n + 1
                else:  # i am taking average by assuming 1st day the person is not absent,i.e, 1st column of any row is not empty
                    df.iloc[i, j] = str(round(float(sum / n), 3))
                    sum = sum + float(df.iloc[i, j])
                y = np.append(y, float(df.iloc[i, j]))
            # print(y)
            f = 0
            ls = [df.iloc[i, 0], '--']
            # print(ls)
            model = LinearRegression().fit(x, y)
            y_pred = model.intercept_ + model.coef_ * (a + 4)  # direct 4th day
            # print(y_pred)
            # df.at[i, p] = y_pred[0]
            ls.append(round(y_pred[0], 3))
            if (y_pred[0] > 100.4):
                f = 1
            if (f == 1):
                file1.write("   ".join([str(s) for s in ls]))
                file1.write("\n")
                count = count + 1

        current_time = time.ctime()
        print(df)
        file1.close()
        # print(current_time)
        logfile = open("log.txt", "a")
        logfile.write("{}   {}\n".format(current_time, count))
        logfile.close()

    @dispatch(str, float)
    def sendMail(self, rnum, temperature):
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

        Student {} is having a predicted temperature of {}
        Please take immediate attention over this issue.

        Thank you
        '''.format(rnum, temperature)  # body of the mail

        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)  # concating the strings using string formatting

        smtpobj.sendmail('covidCloudmp@gmail.com', '1602-19-735-091@vce.ac.in', message)
        # sending the mail from us to the reciever; 071 = user; 091 = reciever; message = subject + body

        smtpobj.quit()  # quiting the smtp server and deleting the object

    @dispatch()
    def sendMail(self):
        # use creds to create a client to interact with the Google Drive API
        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                 "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

        # scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name('credsgss.json', scope)
        client = gspread.authorize(creds)

        # Find a workbook by name and open the first sheet
        # Make sure you use the right name here.
        sheet = client.open("testing").sheet1

        data = sheet.get_all_records()
        # print(data)
        df = pd.DataFrame(data)
        print(df)

    def sendSMS(self,rn,temp):
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
            'numbers': '9605861454',
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

    def run(self):
        day = time.ctime().split(' ')[0]
        today = date.today()
        today = today.strftime("%Y/%m/%d")
        print(today)
        if day == 'Sun':
            print('Monday')
        else:
            self.predict()