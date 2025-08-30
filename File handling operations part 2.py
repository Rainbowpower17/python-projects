amazing_file=open('Codingiscool.txt','x')
amazing_file.close()


import os
print('Checking if the file you want exists or not')
if os.path.exists("Codingiscool.txt"):
    os.remove("Codingiscool.txt")
else:
        print("The file dosent exist")
my_file=open('Codingiscool', 'w')
my_file.write("Hello my name is Abesalat and I am 10 years old")
my_file.close()
