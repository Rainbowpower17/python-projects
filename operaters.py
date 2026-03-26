class A:
    def __init__(self,a):
        self.a=a
    def __lt__(self,other):
        if(self.a<other.a):
            return "ob1 is less than ob2"
        else:
            return "ob2 is lessthan ob1"
    def __eq__(self, other):
        if (self.a == other.a):
            return "Both are equal"
        else:
            return "Not equal"
ob1=A(5)
ob2=A(7)
print(ob1.a<ob2.a)
ob3=A(3)
ob4=A(3)
print(ob3.a==ob4.a)
