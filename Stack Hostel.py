def empty(stack):
    if len(stack)==0:
        return "underflow"

def add(w,x,y,a,b,c):
    w.append(a)
    x.append(b)
    y.append(c)
    top=len(w)-1
def delete(x,y,z):
    a=empty(x)
    b=empty(y)
    c=empty(z)
    if a == "underflow" and b== "underflow" and c== "underflow":
        return "underflow"
    else:
        i=x.pop()
        j=y.pop()
        k=z.pop()
        if len(x)==0 and len(y)==0 and len(z)==0:
            top=None
        else:
            top=len(x)-1
        return i,j,k
    
def display(x,y,z):
    a=empty(x)
    b=empty(y)
    c=empty(z)
    if a == "underflow" and b== "underflow" and c== "underflow":
        print("The Stack is Empty")
    else:
        aa=len(x)-1
        bb=len(y)-1
        cc=len(z)-1
        print("Hostel.No""|""Students""|""Rooms")
        while aa>=0 and bb>=0 and cc>=0:
            print(x[aa],"      ",y[bb],"     ",z[cc])
            aa-=1
            bb-=1
            cc-=1

Hostel=[]
Students=[]
Rooms=[]
top=None
while True:
    print("1:Add")
    print("2:Delete")
    print("3:Display")
    print("4:Exit")
    a=int(input("Enter a Choice: "))
    print()
    if a==1:
        i=int(input("Enter the Hostel Number: "))
        j=int(input("Enter the Total Number of Students: "))
        k=int(input("Enter the Total Number of Rooms: "))
        add(Hostel,Students,Rooms,i,j,k)
    elif a==2:
        i=delete(Hostel,Students,Rooms)
        if i=="underflow":
            print("Stack is Empty")
            print()
        else:
            print("Element Deleted",i)
    elif a==3:
        print()
        display(Hostel,Students,Rooms)
        print()
    elif a==4:
        break
    else:
        print("Enter a Valid Input")
