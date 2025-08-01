phone_book={}

def add_contanct():
    name=input("Enter name:  ").strip()
    phone=input("Enter phone number").strip()
    phone_book[name]=phone
    print(f"Contact '{name}' added")

def view_contacts():
    if not phone_book:
        print("Phone contact is empty")
    else:
        for name, phone in phone_book.items():
            print(f"{name} {phone}")
def search_contact():
    name=input("Enter name to search: ").strip()
    if name in phone_book:
        print(f"{name}  {phone_book[name]}")
    else:
        print("Contanct not found")
def delete_contanct():
    name=input("Enter name to delete").strip()
    if name in phone_book:
        del phone_book[name]   
        print(f"Contanct '{name} deleted'")
    else:
        print("Contanct not found")
def main():
    while True:
        print("\nPhone book menu")
        print("1.Add contanct")
        print("2.View contanct")
        print("3.Search contanct")
        print("4.Delete contanct")
        print("5.Exit")

        choice=input("Enter a phone number (1-5):")
        if choice=="1":
            add_contanct()
        elif choice=="2":
            add_contanct()
        elif choice=="3":
            add_contanct()
        elif choice=="4":
            add_contanct()            
        elif choice=="5":
            print("Good bye")
            break
        print("Invalid choice.Try again ")
main()        
