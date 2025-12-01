age=int(input("Enter your age (0-20)"))
if age>=0 and age<=20:
    if age>=0 and age<=2:
        print("You are a baby")
    elif age>=3 and age<=5:
        print("You are a toddler")
    elif age>=6 and age<=10:
        print("You are a kid")
    elif age>=11 and age<=12:
        print("You are a pre-teen")
    if age>=13 and age<=17:
        print("You are a teen")
        if age>=15 and age<=17:
            print("You are almost an adult")
    elif age==18:
        print("You are an adult")
    elif age>=19 and age<=20:
        print("You are a young adult")
else:
    print("Please enter an age betwen 0-20") 