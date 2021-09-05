
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
det=[]
pastTime16 = round(time.time())
# nowTime = round(time.time())
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
        for F in (StartPage,PageTwo):
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
        logo = Image.open("media/vlogo.png")
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
        details_label = Label(bottom_frame, text='''     Please Scan Your ID Card''', bg='white',
                              font=('Arial Rounded MT Bold', 30),
                              height=5, anchor=CENTER)  # target=self.get_roll  # if out side the __init__
        # details_label.pack(side=TOP)
        details_label.pack(fill='both', expand=True)
        def message():
            details_label['text'] = "     Please Scan Your ID Card"
        def get_roll():
            global roll_num
            roll_num = qr1.readBarcode()
            # rollno.set('')
            ck_roll=BooleanVar(self, name ="bool")
            self.controller.setvar(name="bool",value=qr1.checkRollNo(roll_num))
            print(ck_roll)
            if ck_roll.get()==True:
                global det
                det=qr1.readDbms(roll_num)
                '''global pastTime
                pastTime = round(time.time())
                nowTime = round(time.time())  # for the sending data to gss   # add in gui later
                #if nowTime - pastTime >= 30 * 60:
                t2 = threading.Thread(target=qr1.sendArrangeData)
                t2.start()
                    # global pastTime
                pastTime = round(time.time())
                nowTime = round(time.time())'''


                details_label.pack_forget()
                
                self.img = ImageTk.PhotoImage(
                    (Image.open("{}".format(det[4]))).resize(
                        (150, 180),
                        Image.ANTIALIAS))

                canvas = Canvas(bottom_frame, bg='white', width=150, height=180)
                canvas.pack(fill=X, side='left')
                canvas.create_image(0, 0, anchor=NW, image=self.img)

                stu_det=Label(bottom_frame, text="Student Details", bg='white', font=('Bahnschrift SemiBold', 20))
                stu_det.pack(fill='both')
                text1 = f'''\nName\t{det[1]}\nRoll No.\t{det[0]}\nBranch\t{det[2]} {det[3]}'''
                person = Label(bottom_frame, text=text1, bg='white', font=('Bahnschrift SemiBold', 15), justify=LEFT,
                               height=4,
                               anchor=N)
                person.pack(fill=Y)
                text2 = f'''Please Put Your Hand Close to the\nTemperature Sensor'''

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
                            scanTime = time.localtime()
                            print("Your temperature: ", temp)
                            with open('TempRoll.txt', 'a') as f:  # saves the student data in TempRoll.txt
                                f.write(f'{roll_num}/ {temp}/ {scanTime.tm_hour}:{scanTime.tm_min} \n')
                            tme = f'{scanTime.tm_hour}: {scanTime.tm_min}'
                            '''global pastTime
                            pastTime = round(time.time())
                            nowTime = round(time.time())  # for the sending data to gss   # add in gui later
                            # if nowTime - pastTime >= 30 * 60:
                            t2 = threading.Thread(target=qr1.sendArrangeData,args=(roll_num,temp,tme))
                            t2.start()
                            # global pastTime
                            pastTime = round(time.time())
                            nowTime = round(time.time())'''

                            message1['text'] = f'''Your Temperature:\t{temp}{ds}F\nPlease Enter.\nHave a Nice Day!'''
                            if temp > 100:  # sending mail sms and playing alarm if temp greater than 100
                                t1 = threading.Thread(target=qr1.mailandsms, args=(det[0], temp))
                                t1.start()
                                message1['text'] = f'''Your Temperature:\t{temp}{ds}F\nPlease Don't Enter!'''
                                message1['fg']='red'
                                qr1.Alarm()

                                # t1.join()
                                print('Alarm mail and sms sent')
                            time.sleep(5)
                            print("NEXT")
                            canvas.pack_forget()
                            stu_det.pack_forget()
                            person.pack_forget()       # hiding label
                            details_label.pack()

                            message1['text']=""
                            message1.pack_forget()
                            forpack.pack_forget()
                            roll_pack = Label(bottom_frame, command=threading.Thread(target=get_roll).start())

                        else:
                            message1['text'] = ''' Please Put Your Hand Closer\nto the Sensor'''

                message1 = Label(self, text=text2, fg='blue', font=('Bahnschrift SemiBold', 20))
                message1.pack(fill=Y)
                forpack = Label(self, command=threading.Thread(target=chk_dis).start())
                forpack.pack()
            else:
                details_label['text']="NOT VALID"
                controller.after(2000, message)
                roll_pack = Label(bottom_frame, command=threading.Thread(target=get_roll).start())

            # details_label['text'] = roll_no.get()   # works

        rollpack = Label(bottom_frame,  command=threading.Thread(target=get_roll).start())  
        #rollpack.pack()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        controller.show_frame('StartPage')


if __name__ == "__main__":
    qr1 = p.covidCloud()
    qr2 = pc.cloudPrediction()
    app = SampleApp()
    app.mainloop()
