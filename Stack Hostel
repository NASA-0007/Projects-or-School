def empty(stack):
    if len(stack)==0:
        return "underflow"

def add(w,x,y,z):
    w.append(x),w.append(y),w.append(z)
    top=len(w)-1
def delete(stack):
    a=empty()
    if a=="underflow":
        print("The Stack is Empty")
    else:
        i=stack.pop()
        if len(stack)==0:
            top=None
        else:
            top=len(stack)-1
        return i
    
def display(stack):
    a=empty(stack)
    if a == "underflow":
        print("The Stack is Empty")
    else:
        a=len(stack)-1
        for i in range(a):
            print (stack[a])
            print()
stack=[]
top=None
while True:
    print("1:Add")
    print("2:Delete")
    print("3:Display")
    print("4:Exit")
    a=int(input("Enter a Choice"))
    if a==1:
        i=int(input("Enter the Hostel Number"))
        j=int(input("Enter the Total Number of Students"))
        k=int(input("Enter the Total Number of Rooms"))
        add(stack,i,j,k)
    elif a==2:
        i=delete(stack)
        if i=="underflow":
            print("Stack is Empty")
        else:
            print("Element Deleted",i)
    elif a==3:
        display(stack)
    elif a==4:
        break
    else:
        print("Enter a Valid Input")
