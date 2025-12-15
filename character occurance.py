string=input("Please enter a word of your own")
char=input("Please enter your own character")
i=0
count=0
while(i<len(string)):
    if (string [i] ==char):
        count=count+1
    i=i+1
print('The total Number of times',char,"has occured =",count)