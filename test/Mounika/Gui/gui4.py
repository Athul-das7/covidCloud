#  Don't gelkify this
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import time


det=['1602-19-735-071', 'KUMARANKANDATH ATHUL DAS', 'ECE', 'B', 'media\\71.jpg']
temp=100
ds=u'\N{DEGREE SIGN}'
window = Tk()
window.geometry("800x480")
# top frame for college name and logo
top_frame = LabelFrame(window, bg='white', height=500)
window.resizable(width=False, height=False)    # fixed window size
top_frame.pack(fill=X, side=TOP)
# bottom frame for details
bottom_frame = LabelFrame(window, bg='white', pady=10)
bottom_frame.pack(fill='both')
vlogo = Image.open("D:\\CovidCloud_project\\covidCloud\\main\\prototype\\media\\vlogo.png")
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
    (Image.open("D:\\CovidCloud_project\\covidCloud\\main\prototype\\{}".format(det[4]))).resize((150, 180),
                                                                                                 Image.ANTIALIAS))
canvas = Canvas(bottom_frame, bg='white', width=150, height=180)
canvas.pack(fill=X, side='left')
canvas.create_image(0, 0, anchor=NW, image=img)
Label(bottom_frame, text="Student Details", bg='white', font=('Bahnschrift SemiBold', 20)).pack(fill='both')
text1 = f'''\nName\t{det[1]}\nRoll No.\t{det[0]}\nBranch\t{det[2]} {det[3]}'''
person = Label(bottom_frame, text=text1, bg='white',font=('Bahnschrift SemiBold', 20), justify=LEFT, height=7,anchor=N)
person.pack(fill=Y)
# time.sleep(5)
# text1=f'''Name\t{det[1]}\nRoll No.\t{det[0]}\nBranch\t{det[2]} {det[3]}\nYour Temperature:\t{temp}{ds}F'''
# person['text']=text1
window.mainloop()
