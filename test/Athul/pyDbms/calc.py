from tkinter import *

root = Tk()
root.title("Calculator")

#position of click
pos = 0

#function for normal clicks
def click(n):
  global pos
  inp.insert(pos,n)
  pos += 1

sum = 0

#function to add
def add():
  a = inp.get()
  inp.delete(0,END)
  global sum
  if a == "":
    return sum
  sum += int(a)
  return sum

#function for equal
def eql():
  sum = add()
  inp.insert(0,sum)

#function for clear
def clear():
  global sum
  sum = 0
  inp.delete(0,END)

#input field
inp = Entry(root, width=45, border=10)

#buttons for calculator
but1 = Button(root, text="1", padx=40, pady=20, command = lambda: click(1))
but2 = Button(root, text="2", padx=40, pady=20, command = lambda: click(2))
but3 = Button(root, text="3", padx=40, pady=20, command = lambda: click(3))
but4 = Button(root, text="4", padx=40, pady=20, command = lambda: click(4))
but5 = Button(root, text="5", padx=40, pady=20, command = lambda: click(5))
but6 = Button(root, text="6", padx=40, pady=20, command = lambda: click(6))
but7 = Button(root, text="7", padx=40, pady=20, command = lambda: click(7))
but8 = Button(root, text="8", padx=40, pady=20, command = lambda: click(8))
but9 = Button(root, text="9", padx=40, pady=20, command = lambda: click(9))
but0 = Button(root, text="0", padx=40, pady=20, command = lambda: click(0))
but_add = Button(root, text="+", padx=39, pady=20, command = add)
but_eq = Button(root, text="=", padx=87, pady=20, command = eql)
but_cls = Button(root, text="Clear", padx=78, pady=20, command =clear)

#positioning of buttons
but1.grid(row=3, column=0)
but2.grid(row=3, column=1)
but3.grid(row=3, column=2)

but4.grid(row=2, column=0)
but5.grid(row=2, column=1)
but6.grid(row=2, column=2)

but7.grid(row=1, column=0)
but8.grid(row=1, column=1)
but9.grid(row=1, column=2)

but0.grid(row=4, column=0)

#Mislenaous buttons
but_add.grid(row=5, column=0)
but_cls.grid(row=4, column=1, columnspan=2)
but_eq.grid(row=5, column=1, columnspan=2)

#input field position
inp.grid(row=0,column=0,columnspan=3)

root.mainloop()
