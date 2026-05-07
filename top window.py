from tkinter import *

rooot=Tk()
rooot.geometry('400x300')
rooot.title('Main')

def topwin():

    top=Toplevel(bg='pink')
    top.geometry('180x100')
    top.title('Top')

    label=Label(top, text='This is a popup(top level)')
    label.pack()

    top.mainloop

label2=Label(rooot, text='This is the main window')
btn=Button(rooot,text='Click here to open a popup',command=topwin, relief=RIDGE,fg='pink',bg='orange')
label2.pack()
btn.pack()

rooot.mainloop()