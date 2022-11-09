def empty(stack):
    if len(stack)==0:
        return "underflow"

def add(w,a):
    w.append(a)
    top=len(w)-1
def delete(x):
    a=empty(x)
    if a == "underflow":
        return "underflow"
    else:
        i=x.pop()
        if len(x)==0:
            top=None
        else:
            top=len(x)-1
        return i
def display(x):
  l=len(x)
  print("Hostel Number\tTotal Students\tTotal Rooms")
  for i in range(l-1,-1,-1):
      print(x[i][0],"\t\t",x[i][1],"\t\t",x[i][2])
Hostel=[]
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
        print()
        hh=[i,j,k]
        add(Hostel,hh)
    elif a==2:
        i=delete(Hostel)
        if i=="underflow":
            print("Stack is Empty")
            print()
        else:
            print("Element Deleted",i)
    elif a==3:
        print()
        display(Hostel)
        print()
    elif a==4:
        break
    else:
        print("Enter a Valid Input")
