def empty(stack):
    if len(stack)==0:
        return "underflow"

def add(w,a):
    w.append(a)
    top=len(w)-1

def reverse(x):
    a=empty(x)
    if a == "underflow":
        return "underflow"
    else:
        aa=len(x)
        for i in range(aa):
            k=x.pop()
            return k
        if len(x)==0:
            top=None
        else:
            top=len(x)-1
string=[]
top=None
while True:
    print("1:Add")
    print("2:Delete")
    print("3:Exit")
    a=int(input("Enter a Choice: "))
    print()
    if a==1:
        i=input("Enter the String: ")
        hh=[i]
        for j in range(len(hh)):
            add(string,hh[j])
    elif a==2:
        pp=reverse(string)
        if pp=="underflow":
            print("Stack is Empty")
            print()
        else:
            for i in range(len(hh)):
                print("Element Deleted",i)
    elif a==3:
        break
    else:
        print("Enter a Valid Input")
        print()
