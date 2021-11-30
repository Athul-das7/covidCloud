import tkinter as tk  # python 3
from tkinter import font  as tkfont  # python 3
# import mttkinter
from tkinter import *
from PIL import ImageTk, Image
import threading
import prototypeRasp as p
import prototypeCloud as pc
import time
import concurrent.futures
from multiprocessing import Queue

stop_threads = False
det = []
pastTime16 = round(time.time())
# nowTime = round(time.time())
ds = u'\N{DEGREE SIGN}'
roll_num = ""


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageTwo):
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
        self.controller.geometry("480x320")         # 800*480
        # top frame for college name and logo
        top_frame = LabelFrame(self, bg='white', height=340)     #500
        self.controller.resizable(width=False, height=False)  # fixed window size
        top_frame.pack(fill=X, side=TOP)
        # bottom frame for details
        bottom_frame = LabelFrame(self, bg='white', pady=6)          # 6
        bottom_frame.pack(fill='both')
        # logo
        logo = Image.open("media/vlogo.png")
        resize_image = logo.resize((90, 90), Image.ANTIALIAS)     # 150 150
        # The variable photo is a local variable which gets
        # garbage collected after the class is instantiated. Save a reference to the photo
        self.imge = ImageTk.PhotoImage(resize_image)
        label1 = Label(top_frame, image=self.imge, bg="white")
        label1.pack(side="left")
        myCollegeName = Label(top_frame,
                              text='''Vasavi College of Engineering\nAffiliated to Osmania University and Approved by AICTE\nIbrahimbagh, Hyderabad-5000031\nPH: 23146097 / 23146003''',
                              bg='white', font=('Bahnschrift', 10), pady=15)     # 17, pady = 30
        myCollegeName.pack()
        Label(self.controller, text='''
                  ''').pack()
        details_label = Label(bottom_frame, text='''     Please stand still''', bg='white',
                              font=('Arial Rounded MT Bold', 15),    # 30
                              height=2, anchor=CENTER)  # target=self.get_roll  # if out side the __init__     # 5
        # details_label.pack(side=TOP)
        details_label.pack(fill='both', expand=True)

        def message():
            details_label['text'] = "     Please stand still"

        def get_roll():
            global roll_num
            roll_num = qr1.readBarcode()
            # rollno.set('')

            # beep sound after reading roll no
            # qr1.Alert()       # ------

            ck_roll = BooleanVar(self, name="bool")
            self.controller.setvar(name="bool", value=qr1.checkRollNo(roll_num))
            print(ck_roll)
            if ck_roll.get() == True:
                global det

                det = qr1.readDbms(roll_num)
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
                        (90, 120),                                # 150 180
                        Image.ANTIALIAS))

                canvas = Canvas(bottom_frame, bg='white', width=90, height=120)
                canvas.pack(fill=X, side='left')
                canvas.create_image(0, 0, anchor=NW, image=self.img)

                stu_det = Label(bottom_frame, text="Student Details", bg='white', font=('Bahnschrift SemiBold', 10))      # 20
                stu_det.pack(fill='both')
                text1 = f'''\nName\t{det[1]}\nRoll No.\t{det[0]}\nBranch\t{det[2]} {det[3]}'''
                person = Label(bottom_frame, text=text1, bg='white', font=('Bahnschrift SemiBold', 10), justify=LEFT,    # 15
                               height=4,                    # 4
                               anchor=N)
                person.pack(fill=Y)
                text2 = f'''Please Put Your Hand Close to the Sensor\n'''
                message1 = Label(self, text=text2, fg='blue', font=('Bahnschrift SemiBold', 15))       # 20

                def countdown(count):
                    # change text in label
                    message1['text'] = f'''Please Put Your Hand Close to the Sensor\n{count}'''
                    time.sleep(1)

                    if count >= 2:

                        # call countdown again after 1000ms (1s)
                        # self.after(1000, countdown, count - 1)
                        countdown(count-1)


                # tt1 = threading.Thread(target=countdown, args=[5])
                def chk_temp():
                    cktemp = 0
                    #dist = 2.00
                    temp = 0.00
                    # tt1.start()
                    # print("thread started")
                    countdown(5)
                    while cktemp == 0:
                        # dist = qr1.readDistance()
                        temp = qr1.readTemperature()
                        # qr1.Alarm(2)     # ----------

                        # print(dist, " cm")
                        print("Your temperature: ", temp)
                        cktemp = qr1.checkTemperature(temp)
                        # tt1.start()

                        if cktemp !=0  :

                            # temp = qr1.readTemperature()
                            # tt1.join()

                            # tt1 = threading.Thread(target=countdown, args=[5])
                            # tt1.start()

                            # 2 times beep sound after reading temperature
                            # qr1.Alarm(2)

                            scanTime = time.localtime()
                            print("Your temperature: ", temp)
                            with open('TempRoll.txt', 'a') as f:  # saves the student data in TempRoll.txt
                                f.write(f'{roll_num}/ {temp}/ {scanTime.tm_hour}:{scanTime.tm_min} \n')
                            tme = f'{scanTime.tm_hour}: {scanTime.tm_min}'
                            '''global pastTime
                            pastTime = round(time.time())
                            nowTime = round(time.time())  # for the sending data to gss   # add in gui later
                            # if nowTime - pastTime >= 30 * 60:

                            # global pastTime
                            pastTime = round(time.time())
                            nowTime = round(time.time())'''

                            message1['text'] = f'''Your Temperature:\t{temp}{ds}C\nPlease Enter.\nHave a Nice Day!'''

                            if temp > 37.4:  # sending mail sms and playing alarm if temp greater than 100
                                t1 = threading.Thread(target=qr1.mailandsms, args=(det[0], temp))
                                t1.start()
                                message1['text'] = f'''Your Temperature:\t{temp}{ds}C\nPlease Don't Enter!'''
                                message1['fg'] = 'red'
                                # qr1.Alert()

                                # t1.join()
                                print('Alarm mail and sms sent')
                            time.sleep(10)


                            print("NEXT")
                            canvas.pack_forget()
                            stu_det.pack_forget()
                            person.pack_forget()  # hiding label
                            details_label.pack()

                            message1['text'] = ""
                            message1.pack_forget()
                            forpack.pack_forget()
                            roll_pack = Label(bottom_frame, command=threading.Thread(target=get_roll).start())

                        else:

                            cktemp = 1
                            canvas.pack_forget()
                            stu_det.pack_forget()
                            person.pack_forget()  # hiding label
                            details_label.pack()

                            message1['text'] = ""
                            message1.pack_forget()
                            forpack.pack_forget()
                            # message1['text'] = ''' Please Put Your Hand Closer\nto the Sensor'''
                            # # tt1.raise_exception()
                            # tt1.join()
                            controller.after(2000, message)
                            roll_pack = Label(bottom_frame, command=threading.Thread(target=get_roll).start())


                message1 = Label(self, text=text2, fg='blue', font=('Bahnschrift SemiBold', 15))       # 20
                message1.pack(fill=Y)
                time.sleep(1)


                forpack = Label(self, command=threading.Thread(target=chk_temp).start())
                forpack.pack()
            else:
                details_label['text'] = "NOT VALID"
                controller.after(2000, message)
                roll_pack = Label(bottom_frame, command=threading.Thread(target=get_roll).start())

            # details_label['text'] = roll_no.get()   # works

        rollpack = Label(bottom_frame, command=threading.Thread(target=get_roll).start())
        # rollpack.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        controller.show_frame('StartPage')


if __name__ == "__main__":
    qr1 = p.covidCloud()
    qr2 = pc.cloudPrediction()
    t2 = threading.Thread(target=qr1.sendArrangeData)  # ,args=(roll_num,temp,tme))
    t2.start()
    app = SampleApp()
    app.mainloop()
