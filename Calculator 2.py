def mul(a,b):
    print(a*b)
def sub(c,d):
    print(c-d)
def add(e,f):
    print(e+f)
def div(g,h):
    print(g//h)  
L=int(input("Enter your first number"))
T=int(input("Enter yoursecond number"))
S=input("Enter a sign like +,//,*,-")
if S=="+":
    add(T,L)    
elif S=="-":
    sub(L,T)
elif S=="//":
    div(L,T)    
elif S=="*":
    mul(T,L)
