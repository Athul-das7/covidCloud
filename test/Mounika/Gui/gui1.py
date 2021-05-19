import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
# root.geometry("800x480")
root.resizable(width=False, height=False)    # fix size of window
# to place window at the centre of the screen
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
x_cor=width/2 - 400
y_cor=height/2 - 240
root.geometry("%dx%d+%d+%d" % (800,480,x_cor,y_cor))     # to place window at the centre of the screen
# root.geometry("%dx%d+0+0" % (width, height))      # full screen resolution
# canvas = Canvas(root, width = 300, height = 300)

# top_frame = LabelFrame(root,bg='red',padx=100,pady=100)
top_frame = LabelFrame(root,bg='white',height=200)

top_frame.pack(fill=X,side=TOP)
# top_frame.grid(row=0,column=0,sticky='we')
# b1 = Button(top_frame, text="Apple")
# b1.pack()

# bottom_frame = LabelFrame(root,bg='green',padx=100,pady=120)
bottom_frame = LabelFrame(root,bg='white')

bottom_frame.pack(fill=X)
# bottom_frame.grid(row=1,column=0,sticky='we')
# b1 = Button(bottom_frame, text="Apple")
# b1.pack()
# listbox_object = Listbox(right_frame)
# listbox_object2 = Listbox(right_frame)
# listbox_object.grid(row=0, column=0)
# listbox_object2.grid(row=0, column=2)


vlogo = Image.open("D:\\CovidCloud_project\\covidCloud\\main\\prototype\\media\\vlogo.png")
resize_image = vlogo.resize((150, 150),Image.ANTIALIAS)
imge = ImageTk.PhotoImage(resize_image)
label1 = Label(top_frame, image=imge,bg='white')
# label1.grid(row=0, column=0)
label1.pack(side="left")
myCollegeName=Label(top_frame,text='''Vasavi College of Engineering
Affiliated to Osmania University and Approved by AICTE
Ibrahimbagh, Hyderabad-5000031
PH: 23146097 / 23146003''',bg='white',font=('Bahnschrift', 18),pady=40)
myCollegeName.pack()
# text1=Label(bottom_frame, text='''     Please Scan Your ID Card''',bg='white',font=('Arial Rounded MT Bold', 30),pady=150)
text1=Label(bottom_frame, text='''     Please Scan Your ID Card''',bg='white',font=('Arial Rounded MT Bold', 30),
            height=6,anchor=CENTER)

text1.pack(side=TOP)
root.mainloop()


