import csv
def add():
    f=open("userdet.csv","w")
    u=int(input("How Many Users ? "))
    userdeta=csv.writer(f)
    head=(["User Name","Password"])
    userdeta.writerow(head)
    for i in range(u):
        a=input("Enter the User ID: ")
        b=input("Enter the Password: ")
        print()
        c=([a,b])
        userdeta.writerow(c)
    f.close()
def create():
    fh=open("userdet.csv")
    a=input("Enter the User ID to Search: ")
    userdet=csv.reader(fh)
    for i in userdet:
        g=i[0]
        k=i[1]
        if g == a:
            print("The User With Id:",a,", has Password:",k)
        else:
            pass
    fh.close()

add()
create()
    
