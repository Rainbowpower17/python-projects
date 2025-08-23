file=open('Aboutme.txt', 'r')
print(file.read())
file.close()

file=open('Aboutme.txt','r')
print('\n Read in parts \n')
print(file.read(11))