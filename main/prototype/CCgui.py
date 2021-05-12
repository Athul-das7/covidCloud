'''
logo    VASAVI COLLEGE OF ENGINEERING
logo      non aided since 1970 TL

1) Scan your roll No using barcode
2) Display details else ask him/her to enter again
3) Place hand near the circle
4) 100F > don't get inside or else have a nice day


# Import Module
from tkinter import *
from PIL import Image, ImageTk

# Create Tkinter Object
root = Tk()

# Read the Image
image = Image.open("media\\1.jpg")

# Reszie the image using resize() method
width = 75
height = 100
resize_image = image.resize((width, height))

img = ImageTk.PhotoImage(resize_image)

# create label and add resize image
label1 = Label(image=img)
label1.image = img
label1.pack()

# Execute Tkinter
root.mainloop()
'''
from tkinter import *
from random import *


def background():
    x = randrange(255)
    y = randrange(255)
    z = randrange(255)
    rgb_color = [x, y, z]
    mycolor = '#%02x%02x%02x' % (x, y, z)
    app.configure(bg=mycolor)
    label1.configure(text=rgb_color)


app = Tk()
app.geometry("500x400+5+5")
app.resizable(0, 0)
app.title("Color Code")
button1 = Button(app, text="Change", command=background)
button1.place(x=225,y=210)
label1 = Label(app, text="")
label1.pack()
app.mainloop()