file=open("new.txt", 'r')
print(file.read())
file.close()

file=open('new.txt', 'r')
print(file.read(11))
file.close()

file=open('new.txt', 'r')
print(file.readline)
print(file.readline)
print(file.readline)
print(file.readline)
file.close()

file=open('new.txt', 'r')
for i in file:
    print(i)
file.close()