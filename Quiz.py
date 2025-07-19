Score=0
print("What is the name of the galaxy we live in")
print("A.milkway galaxy \nB.Blackeye galaxy \nC.Andromeda galaxy")
C=input("Choose the correct answer")
if C=="A":
  print("This is the correct answer")
  Score=Score+10
  print("Your score is",Score)
  print("Which one is a dwarf planet")
  print("A.Jupiter \nB.Mars \nC.pluto")
  D=input("Choose the correct answer")
  if D=="C":
    print("This is the correct answer")
    Score=Score+10
    print("Your score is",Score)
  else:
    print("This is the wrong answer")
    print("Your score is",Score)
else:
  print("This is the wrong answer")
  Score=Score-10
  print("Your score is",Score)
