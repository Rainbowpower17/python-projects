from tkinter import *
from tkinter import messagebox

root=Tk()
root.title('Virus Detected')
root.geometry('200x200')

def msg():
    messagebox.showwarning('Alert!','Stop! Virus found')

button=Button(root, text='scan for virus',command=msg)

button.place(x=40, y=80)

root.mainloop()
