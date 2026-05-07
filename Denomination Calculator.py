from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

#----------------------------------------

root=Tk()
root.title('Denomination Calculator')
root.configure(bg='light blue')
root.geometry('650x400')

#----------------------------------------

upload=Image.open('Tkinter Geometry Managers/cash.jpg')
upload=upload.resize((300,300))
image=ImageTk.PhotoImage(upload)

#----------------------------------------

label=Label(root, image=image, bg='light blue')
label.place(x=180, y=20)

label1=Label(root, text='Hey User! Welcome to Denomination Counter Application.',bg='light blue')

label1.place(relx=0.5,y=340, anchor=CENTER)
#----------------------------------------

def msg():
    Msgbox=messagebox.showinfo('Alert','Do you want to calculate the denomination count?')

    if Msgbox=='OK':
        topwin()
#----------------------------------------

button1=Button(root, text="Let's get started!",command=msg,bg='dark blue',fg='white')
button1.place(x=260,y=360)
#----------------------------------------

def topwin():
    top=Toplevel
    top.title('Denomination Calculator')
    top.configure(bg='light grey')
    top.geometry('600x350+50+50')
#----------------------------------------
    label1=Label(top, text='Enter total amount',bg='Light grey')
    entry=Entry(top)
    lbl1=Label(top,text='Here are number of notes for each denomination',bg='light grey')
#----------------------------------------
    l1=Label(top,text='200',bg='light grey')
    l2=Label(top,text='100',bg='light grey')
    l3=Label(top,text='50',bg='light grey')
#----------------------------------------
    t1=Entry(top)
    t2=Entry(top)
    t3=Entry(top)

    def calculator():
        try:
            amount=int(entry.get())

            note200=amount//200
            amount%=200

            note100=amount//100
            amount%=100

            note50=amount//50

            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)

            t1.insert(END,str(note200))
            t2.insert(END,str(note100))
            t3.insert(END,str(note50))
        except ValueError:
            messagebox.showerror('Error','Please enter a vaid number')

    btn=Button(top,text='Calculate',command='calculator',bg='dark blue',fg='white')

    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)

    label1.place(x=140, y=170)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

    top.mainloop()

# -------------------------------
# Start Main Loop
# -------------------------------
root.mainloop()
