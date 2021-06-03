# All the code required to fuction in cloud must be written here...

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
from prettytable import PrettyTable
import os


class cloudPrediction:
    def __init__(self):
        self.df = 0

    def readDataSheets(self):
        #reads data from the google spread sheets and returns it
        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                 "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("credsgss.json",
                                                                 scope)  # creds is a json file which store Api keys for google sheet

        client = gspread.authorize(creds)

        sheet = client.open(
            "testing").sheet1  # parameter given is google sheet name "covidcloud" which stores data
        data = sheet.get_all_records()
        # print(data)
        self.df = pd.DataFrame(data)


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


        if mcol == 62:
            val = sheet.batch_get(['D:BD'])     #get batch data of the spread sheet
            sheet.delete_columns(2,61)
            sheet.add_cols(60)
            print(val)
            for i in val:
                print(i)
                sheet.update('B:BB', i)   #update and change the spread sheet
            sheet.update_cell(1, 1, f'{mrow}:{mcol - 2}')

    # def predict(self,studentData):    # as per student data will be checked later
    def predict(self):                   # this will run only once from main
        # scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
        #          "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
        #
        # creds = ServiceAccountCredentials.from_json_keyfile_name("credsgss.json",
        #                                                          scope)  # creds is a json file which store Api keys for google sheet
        #
        # client = gspread.authorize(creds)
        #
        # sheet = client.open(
        #     "testing").sheet1  # parameter given is google sheet name "covidcloud" which stores data
        # data = sheet.get_all_records()
        # print(data)
        df = self.df # pd.DataFrame(data)
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
        file1.write("Roll no           --    Predicted Tempetature\n")
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

    @dispatch(str)
    def sendMail(self, rnum):
        # send mail to the management when invoked
        f = open('predict_temp.txt', 'r')  # TempRoll.txt is the file that has all the data of rollNo and temp
        data = f.read()
        f.close()
        f = open('predict_temp.txt', 'w')
        f.close()
        data = data.split('\n')
        # print(data)
        x = PrettyTable()  # creating a pretty table instance
        x.field_names = data[0].split('--')  # Adding the fields

        for i in range(1,len(data)):
            if len(data[i]) != 0:
                # print(data[i].split('--'))
                x.add_row(data[i].split('--'))
        # print(x)
        smtpobj = sl.SMTP('smtp.gmail.com', 587)
        # creating a smtp object and connecting to the domain server of mail.outlook.com over the port 587

        # you can remove the print statements from the code, its placed to know the status of code execution

        smtpobj.ehlo()  # this establishes the connection with the server
        smtpobj.starttls()  # this start the ttls encryption in the server
        pswd = 'athulmounika'  # Taking the password as input is safer because if you save it in a script anyone who can access the script will be able to find the password
        smtpobj.login('covidCloudmp@gmail.com', pswd)  # login in to the smtp server

        SUBJECT = 'The predicted Temperatures'  # subject line

        TEXT = '''Dear management,        
The prediction for today are ;
{}
        Thank you
        '''.format(x)  # body of the mail

        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)  # concating the strings using string formatting

        smtpobj.sendmail('covidCloudmp@gmail.com', '1602-19-735-071@vce.ac.in', message)
        # sending the mail from us to the reciever; 071 = user; 091 = reciever; message = subject + body
        print('Mail sent')
        smtpobj.quit()  # quiting the smtp server and deleting the object

    @dispatch()
    def sendMail(self):
        # use creds to create a client to interact with the Google Drive API
        # scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
        #          "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
        #
        # # scope = ['https://spreadsheets.google.com/feeds']
        # creds = ServiceAccountCredentials.from_json_keyfile_name('credsgss.json', scope)
        # client = gspread.authorize(creds)
        #
        # # Find a workbook by name and open the first sheet
        # # Make sure you use the right name here.
        # sheet = client.open("testing").sheet1
        #
        # data = sheet.get_all_records()  # collecting all the data from spreadsheet

        # print(data)
        df = self.df # pd.DataFrame(data) #   Making a dataframe of it
        print(len(df.columns))
        # for i in data:
        #     print(i)

        today = date.today()        # getting todays date - which is for sure a sunday
        today = today.strftime("%Y/%m/%d")
        todayLocation = 0

        for i in df.columns:
            # if "Time" in i:
            #     print("Didn't enter moron")
            #     df.drop(todayLocation+1)
            #     continue
            if i == today:
                break
            else:  todayLocation += 1   # to find todays index
        # print(df.iloc[0,todayLocation])
        # print(df.iloc[:,todayLocation-6*2 :todayLocation])#.to_string())
        # print(df.rows)
        with pd.option_context('display.max_rows', None,
                               'display.max_columns', None,
                               'display.precision', 3,
                               ):       # just for display purposes
            studentData = df.iloc[:, todayLocation - 6 * 2:todayLocation]
            # print(df.iloc[:, todayLocation - 6 * 2:todayLocation])  # .to_string())
        # print(studentData)
        # print(df.iloc[:,0:1])
        studentRollNo = df.iloc[:,0:1]  # collecting the list of roll numbers from df
        # print("length",len(studentData))
        for i in range(len(studentData)):   #   in the length of student data
            # print(studentRollNo.iloc[i,0])
            stdRoll = studentRollNo.iloc[i,0]  #  individual student roll number
            email = "1602-19-735-071"+'@vce.ac.in'# The students mail

            x = PrettyTable()   # creating a pretty table instance
            x.field_names = ["DAY", "Temperature (in F)"]  # Adding the fields
            itr = 0 # for getting only date elements and not time
            for j in studentData.columns:
                if "Time" in j:
                    itr += 1
                    continue
                else :
                    # print(studentData.iloc[i,itr])
                    x.add_row([j,studentData.iloc[i,itr]])  # adding each student date and temperature in x
                itr += 1
            # print(x)
            # print(stdRoll)
            smtpobj = sl.SMTP('smtp.gmail.com', 587)
            # creating a smtp object and connecting to the domain server of mail.outlook.com over the port 587

            # you can remove the print statements from the code, its placed to know the status of code execution

            smtpobj.ehlo()  # this establishes the connection with the server
            smtpobj.starttls()  # this start the ttls encryption in the server
            pswd = 'athulmounika'  # Taking the password as input is safer because if you save it in a script anyone who can access the script will be able to find the password
            smtpobj.login('covidCloudmp@gmail.com', pswd)  # login in to the smtp server

            SUBJECT = 'Weekend report of {}'.format(stdRoll)  # subject line

            TEXT = '''Hey {},        

This is your weekend temperature report....Have a great weekend.
{}

                    Thank you
                    '''.format(stdRoll, x)  # body of the mail
            print(email)
            message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)  # concating the strings using string formatting

            success = smtpobj.sendmail('covidCloudmp@gmail.com', email, message)
            # sending the mail from us to the reciever; 071 = user; 091 = reciever; message = subject + body
            # print(success)
            print('Mail sent')
            smtpobj.quit()


    def sendSMS(self):
        #sends sms to management if flag is true
        # send SMS to the management when invoked
        url = "https://www.fast2sms.com/dev/bulk"  # Using the fast2sms url
        # Create a account in fast2sms with your phone number and copy the headers creditinals
        # Now change the payload to the way you want to send the message.
        f = open('predict_temp.txt', 'r')  # TempRoll.txt is the file that has all the data of rollNo and temp
        data = f.read()
        f.close()
        data = data.split('\n')
        # print(data)
        x = PrettyTable()  # creating a pretty table instance
        x.field_names = data[0].split('--')  # Adding the fields

        for i in range(1,len(data)):
            if len(data[i]) != 0:
                # print(data[i].split('--'))
                x.add_row(data[i].split('--'))
        print(x)

        # payload = "sender_id=FSTSMS&message=Hey%20Athul&language=english&route=p&numbers=9866989137"

        # create a dictionary
        my_data = {
            # Your default Sender ID
            'sender_id': 'FSTSMS',

            # Put your message here!
            'message': '''The predicted temperatures for today is sent in the mail
Thank You.''',

            'language': 'english',
            'route': 'p',

            # You can send sms to multiple numbers
            # separated by comma.
            'numbers': ['9605861454','9866989137'],
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
        self.readDataSheets()
        day = time.ctime().split(' ')[0]
        today = date.today()
        today = today.strftime("%Y/%m/%d")
        print(today)

        if day == 'Sun':
            print('Sending weekend report')
            self.sendMail()  # the weekend report will be sent to the students
        else:
            print('Running ml model over student data')
            self.predict()
            if os.path.getsize('predict_temp.txt'):
                # self.sendSMS()
                self.sendMail('a')

        self.alterSpreadSheet()
        print('Execution completed')