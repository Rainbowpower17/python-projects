with open('amazingggg.txt', "w")as file:
    file.write("Hi my name is penguin I am 1 yr old")
file.close()


with open('amazingggg.txt', 'r')as file:
    data=file.readlines()
    print("Words in the file are")
    for line in data:
        word=line.split()
        print(word)
file.close()        