# my 1st approch to make it changing
#

import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
# import mttkinter
from tkinter import *
from PIL import ImageTk, Image
import threading
import prototypeRasp as p
import prototypeCloud as pc
import time
import concurrent.futures
from multiprocessing import Queue
que=Queue()
det=['1602-19-735-071', 'KUMARANKANDATH ATHUL DAS', 'ECE', 'B', 'media\\71.jpg']
# det=[]
pastTime = round(time.time())
ds=u'\N{DEGREE SIGN}'
roll_num=""

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, DetailsMenu, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title("covidcloud")
        self.controller.geometry("800x480")
        # top frame for college name and logo
        top_frame = LabelFrame(self, bg='white', height=500)
        self.controller.resizable(width=False, height=False)  # fixed window size
        top_frame.pack(fill=X, side=TOP)
        # bottom frame for details
        bottom_frame = LabelFrame(self, bg='white', pady=6)
        bottom_frame.pack(fill='both')
        # logo
        logo = Image.open("media\\vlogo.png")
        resize_image = logo.resize((150, 150), Image.ANTIALIAS)
        # The variable photo is a local variable which gets
        # garbage collected after the class is instantiated. Save a reference to the photo
        self.imge = ImageTk.PhotoImage(resize_image)
        label1 = Label(top_frame, image=self.imge, bg="white")
        label1.pack(side="left")
        myCollegeName = Label(top_frame, text='''Vasavi College of Engineering\nAffiliated to Osmania University and Approved by AICTE\nIbrahimbagh, Hyderabad-5000031\nPH: 23146097 / 23146003''', bg='white', font=('Bahnschrift', 17), pady=30)
        myCollegeName.pack()
        Label(self.controller, text='''
                  ''').pack()
        # qr1=p.covidCloud()
        # roll_no=StringVar(self, name ="str")
        # self.controller.setvar(name="str", value=qr1.readBarcode())
        # print(roll_no.get())
        def get_roll():
            # qr1 = p.covidCloud()
            # roll_no = StringVar(self, name="str")
            # self.controller.setvar(name="str", value=qr1.readBarcode())
            # print(roll_no.get())
            # check roll_no
            global roll_num
            roll_num=rollno.get()
            ck_roll=BooleanVar(self, name ="bool")
            self.controller.setvar(name="bool",value=qr1.checkRollNo(rollno.get()))
            print(ck_roll)
            if ck_roll.get()==True:
                # global det
                # det=qr1.readDbms(roll_num)  #  to be checked
                # with concurrent.futures.ThreadPoolExecutor() as executor:      # i could find another way so
                #     # I have to invoke this in each of the frames using global roll no----- will find soon another way
                #     future = executor.submit(qr1.readDbms, roll_num)
                #     return_value = future.result()
                #     print(return_value)
                #     global det
                #     det=return_value
                # print(det)
                print(roll_num)
                controller.show_frame('DetailsMenu')
            else:
                details_label['text']="NOT VALID"
            # details_label['text'] = roll_no.get()   # works
        details_label = Label(bottom_frame, text='''     Please Scan Your ID Card''', bg='white',
                      font=('Arial Rounded MT Bold', 30),
                      height=5, anchor=CENTER)    #  target=self.get_roll  # if out side the __init__
        # details_label.pack(side=TOP)
        details_label.pack(fill='both',expand=True)
        rollno=StringVar()
        roll_entry=Entry(bottom_frame,textvariable=rollno,width=30)
        roll_entry.focus_set()
        roll_entry.pack(side=TOP)
        # def get_roll():
        enter_button=Button(bottom_frame,text="Enter",command=get_roll,relief='raised',borderwidth=3,width=40,height=3)
        enter_button.pack()



class DetailsMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title("covidcloud")
        self.controller.geometry("800x480")
        # top frame for college name and logo
        top_frame = LabelFrame(self, bg='white', height=500)
        self.controller.resizable(width=False, height=False)  # fixed window size
        top_frame.pack(fill=X, side=TOP)
        # bottom frame for details
        bottom_frame = LabelFrame(self, bg='white', pady=10)
        bottom_frame.pack(fill='both')
        # logo
        logo = Image.open("media\\vlogo.png")
        resize_image = logo.resize((150, 150), Image.ANTIALIAS)
        # The variable photo is a local variable which gets
        # garbage collected after the class is instantiated. Save a reference to the photo
        self.imge = ImageTk.PhotoImage(resize_image)
        label1 = Label(top_frame, image=self.imge, bg="white")
        label1.pack(side="left")
        #    for getting data from dbms
        # t = threading.Thread(target=lambda q, arg1: q.put(qr1.readDbms(arg1)), args=(que, roll_num))
        # t.start()
        # t.join()
        # det = que.get()
        myCollegeName = Label(top_frame,
                              text='''Vasavi College of Engineering\nAffiliated to Osmania University and Approved by AICTE\nIbrahimbagh, Hyderabad-5000031\nPH: 23146097 / 23146003''',
                              bg='white', font=('Bahnschrift', 17), pady=30)
        myCollegeName.pack()
        Label(self.controller, text='''
                          ''').pack()
        self.img = ImageTk.PhotoImage(
            (Image.open("D:\\CovidCloud_project\\covidCloud\\main\prototype\\{}".format(det[4]))).resize((150, 180),
                                                                                                         Image.ANTIALIAS))
        canvas = Canvas(bottom_frame, bg='white', width=150, height=180)
        canvas.pack(fill=X, side='left')
        canvas.create_image(0, 0, anchor=NW, image=self.img)

        Label(bottom_frame, text="Student Details", bg='white', font=('Bahnschrift SemiBold', 20)).pack(fill='both')
        text1 = f'''\nName\t{det[1]}\nRoll No.\t{det[0]}\nBranch\t{det[2]} {det[3]}'''
        person = Label(bottom_frame, text=text1, bg='white', font=('Bahnschrift SemiBold', 15), justify=LEFT, height=4,
                       anchor=N)
        person.pack(fill=Y)
        text2=f'''Please Put Your Hand Close to the\nTemperature Sensor'''
        def chk_dis():
            ckdis = False
            dist = 2.00
            temp = 0.00
            while ckdis != True:
                dist = qr1.readDistance()
                print(dist, " cm")
                ckdis = qr1.checkDistance(dist)
                if ckdis == True:
                    temp = qr1.readTemperature()
                    print(qr1.checkTemperature(temp))
                    message1['text']=f'''Your Temperature:\t{temp}{ds}F'''
                    if temp > 100:  # sending mail sms and playing alarm if temp greater than 100
                        t1 = threading.Thread(target=qr1.mailandsms, args=(det[0], temp))
                        t1.start()
                        message1['text']=f'''Your Temperature:\t{temp}{ds}F\nPlease Don't Enter!'''
                        qr1.Alarm()
                        # self.sendMail(rn,temp)
                        # self.sendSMS(rn,temp)
                        # t1.join()
                        print('Alarm mail and sms sent')
                else:
                    message1['text']=''' Please Put Your Hand Closer\nto the Sensor'''

        message1=Label(self,text=text2,fg='blue',font=('Bahnschrift SemiBold', 20))
        message1.pack(fill=Y)
        forpack=Label(self,command=threading.Thread(target=chk_dis).start())
        # forpack=Label(self,command=chk_dis)
        forpack.pack()



class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller



if __name__ == "__main__":
    qr1 = p.covidCloud()
    qr2 = pc.cloudPrediction()
    app = SampleApp()
    app.mainloop()