try:
    n=int(input("Enter your age"))
    if n%2==0:
        print("The number is even")
    else:
        print("The number is odd")
except ValueError:
    print("Invalid input")