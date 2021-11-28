# this code goes into Raspberry pi 

# test the functionality of you code in athul.py or mounika.py file
# replace the pass and add your function
# use the existing code in the test directory as you see fit from anyones folder and complete the function

'''Import all the necessary libraries as you see fit '''
import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date
import time
import threading
#import winsound
import smtplib as sl      #import the smtp library to send mail through scripts
import requests   #importing the requests library to send html requests
import json
import mysql.connector as sql
from tkinter import *
from PIL import ImageTk,Image
import gui3 as G
import face_recognition
import cv2
import numpy as np
import pickle
from smbus2 import SMBus
from mlx90614 import MLX90614
from gpiozero import Buzzer


class covidCloud:
    def readBarcode(self):
                # This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
        # other example, but it includes some basic performance tweaks to make things run a lot faster:
        #   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
        #   2. Only detect faces in every other frame of video.

        # PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
        # OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
        # specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

        # Get a reference to webcam #0 (the default one)
        video_capture = cv2.VideoCapture(0)

        # Load a sample picture and learn how to recognize it.
        # obama_image = face_recognition.load_image_file("athul.jpg")
        # obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

        # # Load a second sample picture and learn how to recognize it.
        # biden_image = face_recognition.load_image_file("mouni.jpeg")
        # biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

        # Create arrays of known face encodings and their names
        with open(f"Encodings.pickle",'rb') as file:
            known_face_encodings = pickle.load(file)
        # = [
        #     obama_face_encoding,
        #     biden_face_encoding
        # ]
        known_face_names = list(known_face_encodings.keys())
        known_face_encodings = np.array(list(known_face_encodings.values()))
        # = [
        #     "Athul Das",
        #     "Mounika"
        # ]

        # Initialize some variables
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True
        past = time.time()
        now = time.time()

        while now-past > 5:
            # Grab a single frame of video
            ret, frame = video_capture.read()

            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]

            # Only process every other frame of video to save time
            if process_this_frame:
                # Find all the faces and face encodings in the current frame of video
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                face_names = []
                for face_encoding in face_encodings:
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    name = "Unknown"

                    # # If a match was found in known_face_encodings, just use the first one.
                    # if True in matches:
                    #     first_match_index = matches.index(True)
                    #     name = known_face_names[first_match_index]

                    # Or instead, use the known face with the smallest distance to the new face
                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = known_face_names[best_match_index]

                    face_names.append(name)
                    print(name)

            process_this_frame = not process_this_frame


            # Display the results
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                # Draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                # Draw a label with a name below the face
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            # Display the resulting image
            cv2.imshow('Video', frame)

            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release handle to the webcam
        video_capture.release()
        cv2.destroyAllWindows()

    def checkRollNo(self, rnum):
        # checks the data recived from barcode scanner and returns true or false
        # received form function readBarcode()
        try:
            num = rnum.split('-')
            f=True
            if int(num[0]) != 1602: f = False
            if int(num[1]) not in range(17, 21) == True:
                f = False
            if int(num[2]) not in range(732,739) == True:
                f = False
            if int(num[3]) not in range(1, 181) == True:
                f = False
            #roll no in the range 1602-19-735-001 to 1602-19-735-180 are valid
            '''if int(num[3]) not in range(1, 121):
                f = False
            if rnum[:12] != '1602-19-735-':
                f = False'''
        except:
            f = False
        if f == True:
            print("Valid")
            #print("please put your hand near temperature sensor")
            return True
        else:
            print("Invalid Id")
            return False

    def readDistance(self):
        # reads the distance using ultrasonic sensor and returns it
        # for now generating random distance
        '''print("please put your hand near temperature sensor")
        testgui = G.details()   #testing
        testgui.message2()
        d = round(2 + (6)*random.random())'''     # min + (max-min)*random.random()  , here  generates in range 2-8
        d = input("Enter distance: ")
        print("Distance: ",d)
        return int(d)

    def checkDistance( self, distance ):
        # checks the distance and returns true or false as per the data given
        if 2 <= distance <= 6:
            return True
        else: return False

    def readTemperature(self):
        bus = SMBus(1)
        sensor = MLX90614(bus, address=0x5A)
        amb = (sensor.get_ambient())
        body = (sensor.get_object_1())
        bus.close()

    def checkTemperature( self, temperature ):
        # check the temperature and return true or false as per the condition
        if ( temperature < 100 and temperature > 94 ):
            return True
        else :
            return False

    def Alarm(self, c):
        # if the function is invoked the alarm must go off for set amout of time

        # print('Playing alarm')
        # for i in range(5):
        #     duration = 1000  # milliseconds
        #     freq = 5040  # Hz
        #     winsound.Beep(freq, duration)
        #     time.sleep(0.5)
        buzzer = Buzzer(26)  # Gpio26  37th pin
        if (c == 1):
            while (c):
                buzzer.beep()
                c -= 1
        else:
            while (c):
                buzzer.beep()
                c-=1

    def Alert(self):
        buzzer = Buzzer(26)  # Gpio26  37th pin
        c = 4
        while (c):
            buzzer.on()
            sleep(1)
            buzzer.off()
            sleep(1)
            c -= 1



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
        print("Mail sent to the management")
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
            'numbers':   '9605861454', # '9866989137',
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
        print("Sms sent to the management")
        #print(returned_msg['message'])

    def sendArrangeData(self): #,rollno,temp,ttime):
        while "12:15:" not in time.ctime() :
            #print(time.ctime())
            time.sleep(30)
        # send the data to google spread sheets and arrange it accordingly
        '''Connect to the spread sheet'''
        # use creds to create a client to interact with the Google Drive API
        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                 "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

        # scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name('credsgss.json', scope)
        client = gspread.authorize(creds)

        # Find a workbook by name and open the first sheet
        # Make sure you use the right name here.
        sheet = client.open("testing").sheet1

        today = date.today()
        today = today.strftime("%Y/%m/%d")
        #today ="2021/05/21"
        # print(type(today))

        FirstCell = sheet.cell(1, 1).value  # first cell contains the max row and max column number
        print(FirstCell)
        mrow, mcol = FirstCell.split(':')
        mrow = int(mrow)  # max row count
        mcol = int(mcol)  # max column count

        try:
            todCol = sheet.find(today).col  # column for today
        except:
            sheet.update_cell(1, mcol, today)
            sheet.update_cell(1, mcol+1, 'Time')
            todCol = mcol  # column for today
            mcol += 2
            sheet.update_cell(1, 1, f'{mrow}:{mcol}')  # update the cell in (1,1) to new value

        f = open('TempRoll.txt', 'r')   #TempRoll.txt is the file that has all the data of rollNo and temp
        data = f.read()
        f.close()
        f = open('TempRoll.txt', 'w')
        f.close()
        data = data.split('\n')
        #print(data)
        time.sleep(2)
        past = time.time()
        now = time.time()
        for i in data:
            if i == '':
                 continue
            now = time.time()
            rollno,temp,ttime = i.split('/')
            try:
                todRow = sheet.find(rollno).row  # Row corresponding to roll no. of student
            except:
                todRow = mrow  # Row corresponding to roll no. of student
                sheet.update_cell(mrow, 1, rollno)
                mrow += 1
                sheet.update_cell(1, 1, f'{mrow}:{mcol}')  # updating the cell (1,1) to the new values

            if now - past > 15:     # runs for 15 secs and sleeps for 40 secs
                # print('Sleep for 40secs')
                time.sleep(40)
                past = time.time()
                now = time.time()
            val = sheet.update_cell(todRow, todCol, temp)
            val = sheet.update_cell(todRow, todCol+1, ttime)
            # print(val)

    def readDbms(self,rn):
        db = sql.connect(
            host="localhost",  # 127.0.0.0/ You don't have to change this.
            user="root",  # connecting to your user/ if you have different user mention
            passwd="Mouni_passsql21",  # entering the password/ change it to your password
            database="vce_db"  # connecting to the database/ Don't change this

        )
        # Nothing from hear on out must be changed
        cur = db.cursor()

        cur.execute('''SELECT *  FROM student_list
        WHERE roll_no = %s ''', (rn,))
        try:
            rows = cur.fetchall()
            rows = list(rows[0])
        except:
            rows=[rn,'--','--','--','media/default_user.jpg']
        db.close()
        return rows

    def showImg(self,path):
        root = Tk()
        # root.geometry("500x300")

        canvas = Canvas(root, width=300, height=300)
        # canvas.pack(padx=25,pady=10)
        canvas.grid(row=1, column=0)
        img = ImageTk.PhotoImage(Image.open(path))
        canvas.create_image(0, 20, anchor=NW, image=img)
        root.mainloop()

    def mailandsms(self,rn,temp):
        self.sendSMS(rn,temp)
        self.sendMail(rn,temp)

    def run(self):
        pastTime = round(time.time())
        while True:
            nowTime = round(time.time())
            if nowTime - pastTime  >= 30*60 :
                t2 = threading.Thread(target=self.sendArrangeData)
                t2.start()
                pastTime = round(time.time())
                nowTime = round(time.time())
            rn = self.readBarcode()
            if self.checkRollNo(rn):
                details = self.readDbms(rn)
                print('Name: ', details[1])
                print('Roll no: ', details[0])
                print('Branch: ', details[2], "-", details[3])
                print('Image: ', details[4])
                self.showImg(details[4])
            i = 5
            while i > 0:
                dist = self.readDistance()
                print(dist)
                if self.checkDistance(dist):
                    temp = self.readTemperature()
                    # scanTime=time.localtime()
                    # print("Your temperature: ", temp)
                    # with open('TempRoll.txt', 'a') as f:  # saves the student data in TempRoll.txt
                    #     f.write(f'{rn}/ {temp}/ {scanTime.tm_hour}:{scanTime.tm_min} \n')
                    if self.checkTemperature(temp):
                        print("You may enter. Have A nice day!")
                        break
                    else:
                        print("Don't enter the campus")
                        t1 = threading.Thread(target=self.mailandsms, args=(rn, temp))
                        t1.start()
                        self.Alarm()
                        # self.sendMail(rn,temp)
                        # self.sendSMS(rn,temp)
                        t1.join()
                        print('Alarm mail and sms sent')
                        break
                else:
                    i -= 1


'''self.sendArrangeData()
        count = 0
        while True:
            if count == 40:
                break
            rn = self.readBarcode()
            if self.checkRollNo(rn):
                details = self.readDbms(rn)
                print('Name: ', details[1])
                print('Roll no: ', details[0])
                print('Branch: ', details[2],"-",details[3])
                print('Image: ', details[4])
                #self.showImg(details[4])
                count+=1
                i = 5
                while i > 0 :
                    dist = self.readDistance()
                    print(dist)
                    if self.checkDistance(dist):
                        temp = self.readTemperature()
                        print("Your temperature: ",temp)
                        with open('TempRoll.txt', 'a') as f: #saves the student data in TempRoll.txt
                            f.write(f'{rn}: {temp}\n')
                        if self.checkTemperature(temp):
                            print("You may enter. Have A nice day!")
                            break
                        else :
                            print("Don't enter the campus")
                            #self.Alarm()
                            #self.sendMail(rn,temp)
                            #self.sendSMS(rn,temp)
                            print('Alarm mail and sms')
                            break
                    else :
                        i -= 1

# the dbms and gui can be added later to this class...or we can make use of another class for gui...
'''
'''oh no no no no'''
