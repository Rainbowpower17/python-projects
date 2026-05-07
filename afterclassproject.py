from tkinter import *
import re

root=Tk()
root.geometry('400x250')
root.title('Password Strength Checker')
root.configure(bg='light blue')

title=Label(root,fg='dark blue',text='Password Strength Checker',font=('Comic sans',12,'bold'))

password_label=Label(root,fg='dark blue',text='Enter password',font=('Comic sans',12,'bold'))

password_entry=Entry(root,width=30,show='*',)

password_entry.pack(pady=10)

result_label = Label(root,text="",font=("Arial", 12, "bold"),bg="lightblue")

result_label.pack(pady=10)

def check_strength():

    strength=0

    password=password_label.get()

    if len(password)>=8:
        strength=+1

    if re.search(r'[A-Z]'):
        strength=+1

    if re.search(r'[a-z]'):
        strength=+1

    if re.search(r'[!@#$%^&*()-{}\|?/]'):
        strength=+1

    if re.search(r'[0-9]'):
        strength=+1

    if strength <= 2:
        result_label.config(
            text="Weak Password",
            fg="red"
        )

    elif strength == 3 or strength == 4:
        result_label.config(
            text="Medium Password",
            fg="orange"
        )

    else:
        result_label.config(
            text="Strong Password",
            fg="green"
        )

# ----------------------------

check_button = Button(
    root,
    text="Check Strength",
    command=check_strength,
    bg="darkblue",
    fg="white",
    font=("Arial", 12)
)

check_button.pack(pady=10)

# ----------------------------

root.mainloop()     