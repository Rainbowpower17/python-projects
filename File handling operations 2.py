new_file=open('I love flowers.txt','x')
new_file.close()


import os
print('Checking if file exists or not')
if os.path.exists("I love flowers.txt"):
    os.remove("I love flowers.txt")
else:
        print("The file dosent exist")
my_file=open('I love flowers.txt', 'w')
my_file.write("Hello my name is penguin and I am 1 yr old")
my_file.close()


os.remove ("I love flowers.txt")