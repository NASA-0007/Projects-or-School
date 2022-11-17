def empty(stack):
    if len(stack)==0:
        return "underflow"
def add(w,a):
    w.append(a)
    top=len(w)-1
def reverse(stack):
    a=empty(stack)
    if a=="underflow":
        print("The Stack is Empty")
    else:
        b=len(stack)
        for i in range(b):
            g=stack.pop()
            if len(stack)==0:
                top=None
            else:
                top=len(stack)-1
            return g
string=[]
rev=[*string]
top=None
while True:
    print("1:Add")
    print("2:Reverse")
    print("3:Exit")
    ch=int(input("Enter a Choice: "))
    if ch==1:
        a=input("Enter a String")
        add(string,a)
    elif ch==2:
        ll=len(string)
        for j in range(ll):
            aa=reverse(string)
            print(aa)
    elif ch==3:
        break
    else:
        print("Enter a Valid Input")
