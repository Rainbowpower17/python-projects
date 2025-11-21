Amount=int(input("Please enter amount for withdraw"))
a=Amount//100
b=(Amount%100)//50
c=((Amount%100)%50)//10
print("notes of 100$", a)
print("notes of 50$", b)
print("notes of 10$", c)