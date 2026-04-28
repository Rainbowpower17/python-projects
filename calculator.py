from tkinter import *

root = Tk()
root.title('Claculator')
root.geometry('400x600')



button7 = Button(root, text="7", relief=RIDGE,bd=10,  height=3,width=7,fg='orange',bg='pink')
button7.place(x=20, y=20)

button8 = Button(root, text="8", relief=RIDGE,bd=10,  height=3,width=7,fg='orange',bg='pink')
button8.place(x=120, y=20)

button9 = Button(root, text="9", relief=RIDGE,bd=10,  height=3,width=7,fg='orange',bg='pink')
button9.place(x=225, y=20)

button_divide = Button(root, text="÷", relief=RIDGE,bd=10,  height=3,width=7,fg='orange',bg='pink')
button_divide.place(x=320, y=20)

button4 = Button(root, text="4", relief=RIDGE,bd=10,  height=3,width=7,fg='orange',bg='pink')
button4.place(x=20, y=100)

button5 = Button(root, text="5", relief=RIDGE,bd=10,  height=3,width=7,fg='orange',bg='pink')
button5.place(x=120, y=100)

button6 = Button(root, text="6", relief=RIDGE,bd=10,  height=3,width=7,fg='orange',bg='pink')
button6.place(x=225, y=100)

button_multiply = Button(root, text="X", relief=RIDGE,bd=10,  height=3,width=7,fg='orange',bg='pink')
button_multiply.place(x=320, y=100)

button1 = Button(root, text="1", relief=RIDGE,bd=10,  height=3,width=7,fg='orange',bg='pink')
button1.place(x=20, y=180)

button2 = Button(root, text="2", relief=RIDGE,bd=10,  height=3,width=7,fg='orange',bg='pink')
button2.place(x=120, y=180)

button3 = Button(root, text="3", relief=RIDGE,bd=10,  height=3,width=7,fg='orange',bg='pink')
button3.place(x=225, y=180)

button_minus = Button(root, text="-", relief=RIDGE,bd=10,  height=3,width=7,fg='orange',bg='pink')
button_minus.place(x=320, y=180)

button0 = Button(root, text="0", relief=RIDGE,bd=10,  height=3,width=7,fg='orange',bg='pink')
button0.place(x=20, y=260)

button_dot = Button(root, text=".", relief=RIDGE,bd=10,  height=3,width=7,fg='orange',bg='pink')
button_dot.place(x=120, y=260)


button_equal = Button(root, text="=", relief=RIDGE,bd=10,  height=3,width=7,fg='orange',bg='pink')
button_equal.place(x=225, y=260)

button_plus = Button(root, text="+", relief=RIDGE,bd=10,  height=3,width=7,fg='orange',bg='pink')
button_plus.place(x=320, y=260)

root.mainloop()