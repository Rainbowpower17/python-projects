medical_cause=input("Did you have a medical cause Yes or No")
atten=int(input("Enter the attendance for the student"))
if medical_cause=='yes':
    print("You are allowed")
else:
    if atten>=75:
        print("Allowed")
    else:
        print("Not allowed")