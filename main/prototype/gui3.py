import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

class details:
    def det_image(self,det):
        window = Tk()
        window.geometry("800x480")
        top_frame = LabelFrame(window, bg='white', height=500)

        top_frame.pack(fill=X, side=TOP)

        bottom_frame = LabelFrame(window, bg='white', pady=10)

        bottom_frame.pack(fill='both')
        vlogo = Image.open("media\\vlogo.png")
        resize_image = vlogo.resize((150, 150), Image.ANTIALIAS)
        imge = ImageTk.PhotoImage(resize_image)
        label1 = Label(top_frame, image=imge, bg='white')
        # label1.grid(row=0, column=0)
        label1.pack(side="left")
        myCollegeName = Label(top_frame, text='''Vasavi College of Engineering
        Affiliated to Osmania University and Approved by AICTE
        Ibrahimbagh, Hyderabad-5000031
        PH: 23146097 / 23146003''', bg='white', font=('Bahnschrift', 18), pady=30)
        myCollegeName.pack()
        Label(window, text='''
          ''').pack()
        img = ImageTk.PhotoImage(
            (Image.open("{}".format(det[4]))).resize((150, 180), Image.ANTIALIAS))
        canvas = Canvas(bottom_frame, bg='white', width=150, height=180)
        canvas.pack(fill=X, side='left')
        canvas.create_image(0, 0, anchor=NW, image=img)
        Label(bottom_frame, text="Student Details", bg='white', font=('Bahnschrift SemiBold', 20)).pack(fill='both')
        text1 = f'''Name\t{det[1]}\nRoll No.\t{det[0]}\nBranch\t{det[2]} {det[3]}'''
        person = Label(bottom_frame, text=text1, bg='white', font=('Bahnschrift SemiBold', 20), justify=LEFT, pady=5)
        person.pack(fill=Y)
        window.mainloop()

    def det_temp(self,det,temp):
        window = Tk()
        window.geometry("800x480")
        top_frame = LabelFrame(window, bg='white', height=500)

        top_frame.pack(fill=X, side=TOP)

        bottom_frame = LabelFrame(window, bg='white', pady=10)

        bottom_frame.pack(fill='both')
        vlogo = Image.open("media\\vlogo.png")
        resize_image = vlogo.resize((150, 150), Image.ANTIALIAS)
        imge = ImageTk.PhotoImage(resize_image)
        label1 = Label(top_frame, image=imge, bg='white')
        # label1.grid(row=0, column=0)
        label1.pack(side="left")
        myCollegeName = Label(top_frame, text='''Vasavi College of Engineering
        Affiliated to Osmania University and Approved by AICTE
        Ibrahimbagh, Hyderabad-5000031
        PH: 23146097 / 23146003''', bg='white', font=('Bahnschrift', 18), pady=30)
        myCollegeName.pack()
        Label(window, text='''
          ''').pack()
        img = ImageTk.PhotoImage(
            (Image.open("{}".format(det[4]))).resize((150, 180),Image.ANTIALIAS))
        canvas = Canvas(bottom_frame, bg='white', width=150, height=180)
        canvas.pack(fill=X, side='left')
        canvas.create_image(0, 0, anchor=NW, image=img)
        Label(bottom_frame, text="Student Details", bg='white', font=('Bahnschrift SemiBold', 20)).pack(fill='both')
        ds=u'\N{DEGREE SIGN}'
        if(temp>100):
            text1 = f'''Name\t{det[1]}\nRoll No.\t{det[0]}\nBranch\t{det[2]} {det[3]}\nYour Temperature:\t{temp}{ds}F\nPlease Don't Enter'''
        else:
            text1=f'''Name\t{det[1]}\nRoll No.\t{det[0]}\nBranch\t{det[2]} {det[3]}\nYour Temperature:\t{temp}{ds}F'''
        person = Label(bottom_frame, text=text1, bg='white', font=('Bahnschrift SemiBold', 20), justify=LEFT, pady=5)
        person.pack(fill=Y)
        window.mainloop()
    def message1(self,):
        root = Tk()
        root.geometry("800x480")
        top_frame = LabelFrame(root, bg='white', height=200)
        top_frame.pack(fill=X, side=TOP)
        bottom_frame = LabelFrame(root, bg='white')
        bottom_frame.pack(fill=X)
        vlogo = Image.open("media\\vlogo.png")
        resize_image = vlogo.resize((150, 150), Image.ANTIALIAS)
        imge = ImageTk.PhotoImage(resize_image)
        label1 = Label(top_frame, image=imge, bg='white')
        # label1.grid(row=0, column=0)
        label1.pack(side="left")
        myCollegeName = Label(top_frame, text='''Vasavi College of Engineering
        Affiliated to Osmania University and Approved by AICTE
        Ibrahimbagh, Hyderabad-5000031
        PH: 23146097 / 23146003''', bg='white', font=('Bahnschrift', 18), pady=40)
        myCollegeName.pack()
        text1 = Label(bottom_frame, text='''     Please Scan Your ID Card''', bg='white',
                      font=('Arial Rounded MT Bold', 30), pady=150)
        text1.pack(side=TOP)
        root.mainloop()
    def message2(self,):
        root = Tk()
        root.geometry("800x480")
        top_frame = LabelFrame(root, bg='white', height=200)
        top_frame.pack(fill=X, side=TOP)
        bottom_frame = LabelFrame(root, bg='white')
        bottom_frame.pack(fill=X)
        vlogo = Image.open("media\\vlogo.png")
        resize_image = vlogo.resize((150, 150), Image.ANTIALIAS)
        imge = ImageTk.PhotoImage(resize_image)
        label1 = Label(top_frame, image=imge, bg='white')
        # label1.grid(row=0, column=0)
        label1.pack(side="left")
        myCollegeName = Label(top_frame, text='''Vasavi College of Engineering
        Affiliated to Osmania University and Approved by AICTE
        Ibrahimbagh, Hyderabad-5000031
        PH: 23146097 / 23146003''', bg='white', font=('Bahnschrift', 18), pady=40)
        myCollegeName.pack()
        text1 = Label(bottom_frame, text='''     Please Put Your Hand Near \nTemperature Sensor''', bg='white',
                      font=('Arial Rounded MT Bold', 25), pady=150)
        text1.pack(side=TOP)
        root.mainloop()

    def message3(self,):
        root = Tk()
        root.geometry("800x480")
        top_frame = LabelFrame(root, bg='white', height=200)
        top_frame.pack(fill=X, side=TOP)
        bottom_frame = LabelFrame(root, bg='white')
        bottom_frame.pack(fill=X)
        vlogo = Image.open("media\\vlogo.png")
        resize_image = vlogo.resize((150, 150), Image.ANTIALIAS)
        imge = ImageTk.PhotoImage(resize_image)
        label1 = Label(top_frame, image=imge, bg='white')
        # label1.grid(row=0, column=0)
        label1.pack(side="left")
        myCollegeName = Label(top_frame, text='''Vasavi College of Engineering
        Affiliated to Osmania University and Approved by AICTE
        Ibrahimbagh, Hyderabad-5000031
        PH: 23146097 / 23146003''', bg='white', font=('Bahnschrift', 18), pady=40)
        myCollegeName.pack()
        text1 = Label(bottom_frame, text='''     Please Put Your Hand Closer\nto the Sensor''', bg='white',
                      font=('Arial Rounded MT Bold', 25), pady=150)
        text1.pack(side=TOP)
        root.mainloop()
