rowsize=int(input('Enter the number of rows'))
if rowsize%2==0:
    half_diamrow=int(rowsize/2)
else:
    half_diamrow=int(rowsize/2)+1
space=half_diamrow-1
for i in range(1, half_diamrow+1):
    for j in range(1,space+1):
        print(end="")
    space=space-1
    num=1
    for j in range(2*i-1):
        print(end=str(num))
        num=num+1
    print()
space=1
for i in range(1,half_diamrow):
    for j in range(1,space+1):
        print(end="")
    space=space+1
    num=1
    for j in range(1,2*(half_diamrow-i)):
        print(end=str(num))
        num=num+1
print()        