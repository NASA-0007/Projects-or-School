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
        b=0
        while aa!=b:
            k=x.pop()
            b+=1
            if len(x)==0:
                top=None
            else:
                top=len(x)-1
            return k
string=[]
top=None
while True:
    print("1:Add")
    print("2:Reverse")
    print("3:Exit")
    a=int(input("Enter a Choice: "))
    print()
    if a==1:
        i=input("Enter the String: ")
        tt=0
        hh=[*i]
        
        while len(hh)!=tt:
            sa=hh[tt]
            add(string,sa)
            tt+=1
        qq=(" ")
        string.append(qq)
        
    elif a==2:
        pp=reverse(string)
        ww=len(string)
        gg=0
        got=True
        if pp=="underflow":
            print("Stack is Empty")
            got=False
            print()
        elif got==True:
            x=[]
            while ww!=gg:
                uu=reverse(string)
                x.append(uu)
                gg+=1
            d=""
            for lu in x:
                d+=lu
            print(d)
                
    elif a==3:
        break
    else:
        print("Enter a Valid Input")
        print()
