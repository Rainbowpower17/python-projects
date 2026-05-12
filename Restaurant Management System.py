import tkinter as tk
from tkinter import ttk, messagebox

class ResturantApp:

    def __init__(self,root):
        self.root=root
        self.root.title('Restuarant App')
        self.root.geometry('500x400')

        
        self.menu = {

        "Burger": 3,

        "Pizza": 4,

        "Fries": 2,

        "Drinks": 1

        }

        self.entries={}

        ttk.Label(root, text='Resturant Order Managment',font=('Arial',16,'bold')).pack(pady=10)


        frame=ttk.Frame(root)
        frame.pack()

        for item, price in self.menu.items():

            row=ttk.Frame(frame)
            row.pack(pady=5)

            ttk.Label(row,text=f'{item} $ {price}',width=20).pack(side='left')

            entry=ttk.Entry(row, width=5)
            entry.pack(side='left')

            self.entries[item]=entry

            ttk.Button(root, text='Place Order',command=self.place_order).pack(pady=20)

    def place_order(self):

        total = 0
        summary = "Order Summary\n\n"

        for item, entry in self.entries.items():

            qty = entry.get()

            if qty.isdigit():

                qty = int(qty)

                if qty > 0:

                    cost = qty * self.menu[item]
                    total += cost

                    summary += f"{item} x {qty} = $ {cost}\n"

        if total > 0:

            summary += f"\nTotal Cost = $ {total}"

            messagebox.showinfo("Order Placed", summary)

        else:
            messagebox.showerror(
                "Error",
                "Please order at least one item"
            )

# Run app
root = tk.Tk()
app =ResturantApp(root)
root.mainloop()            