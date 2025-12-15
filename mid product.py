num = int(input("Enter the number : "))
t = num
numLen = 0

# iterate the loop
while t > 0:
    numLen = numLen + 1
    t = int(t / 10)

# condition 1
if numLen >= 4:
    numLen = int(numLen / 2)
    chk = 0

    while num:  # iterate loop
        rem = num % 10

        if chk == numLen:  # nested condition 1
            midOne = rem
        elif chk == (numLen - 1):
            midTwo = rem

        num = int(num / 10)
        chk = chk + 1

    prod = midOne * midTwo  # product of middle digits

    # display the result
    print("\nProduct of Mid digits (" + str(midOne) + "*" + str(midTwo) + ") = ", prod)
