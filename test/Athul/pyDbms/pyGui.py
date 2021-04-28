from tkinter import *
from PIL import ImageTk,Image
root = Tk()
#root.geometry("500x300")

canvas = Canvas(root, width = 300, height = 300)
logo = Canvas(root, width = 300, height = 300)
myCollegeName=Label(root,text='''Vasavi College of Engineering
Affiliated to Osmania University and Approved by AICTE.''',pady=0)
myCollegeName.grid(row=0,column=1)
#canvas.pack(padx=25,pady=10)
canvas.grid(row=1,column=0)
logo.grid(row=0,column=0)
img = ImageTk.PhotoImage(Image.open("E:\\RollNo\\media\\64.jpg"))
vlogo = ImageTk.PhotoImage(Image.open("E:\\RollNo\\media\\vlogo.gif"))
canvas.create_image(0, 20, anchor=NW, image=img)
logo.create_image(0, 0, anchor=NW, image=vlogo)
root.mainloop()
