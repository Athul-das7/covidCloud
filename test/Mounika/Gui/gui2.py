#  don't gelkify this

# import tkinter as tk
# from tkinter import *
# from PIL import ImageTk, Image
#
# root = Tk()
# root.geometry("800x480")
#
# # root.configure(bg='white')
# # width=root.winfo_screenwidth()
# # height=root.winfo_screenheight()
# # root.geometry("%dx%d+0+0" % (width, height))      # full screen resolution
# # canvas = Canvas(root, width = 300, height = 300)
# # logo = Canvas(root, width = 300, height = 300)
# top_frame=Frame(root)
# top_frame.grid(row=0, column=0)
# bottom_frame=Frame(root)
# bottom_frame.grid()
# vlogo = Image.open("D:\\CovidCloud_project\\covidCloud\\main\\prototype\\media\\vlogo.png")
# resize_image = vlogo.resize((140, 140),Image.ANTIALIAS)
# imge = ImageTk.PhotoImage(resize_image)
# label1 = Label(top_frame, image=imge)
# label1.grid(row=0, column=0)
# myCollegeName=Label(top_frame,text='''Vasavi College of Engineering
# Affiliated to Osmania University and Approved by AICTE
# Ibrahimbagh, Hyderabad-5000031
# PH: 23146097 / 23146003''',font=('Bahnschrift', 15),pady=0)
# text1=Label(bottom_frame, text='''
#
#              Please Scan Your ID Card''',font=('Arial Rounded MT Bold', 25),
#              padx=20)
#
# myCollegeName.grid(row=0,column=5)
# text1.config(anchor=CENTER)
# text1.pack()
#
# label1.mainloop()
#
# from tkinter import * # don't use star imports they flood the namespace

import tkinter as tk
import threading

class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()

    def run(self):
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)

        label = tk.Label(self.root, text="Hello World")
        label.pack()
        # t1=threading.Thread(target=self.ap()).start()
        self.root.mainloop()




app = App()
print('Now we can continue running code while mainloop runs!')

for i in range(100000):
    print(i)
