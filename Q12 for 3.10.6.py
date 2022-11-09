import csv
def add():
    f = open(r"userdet.csv", "w")
    u = int(input("How Many Users ? "))
    userdeta = csv.writer(f)
    head = (["User ID", "Password"])
    userdeta.writerow(head)
    for i in range(u):
        a = input("Enter the User ID: ")
        b = input("Enter the Password: ")
        print()
        c = ([a, b])
        userdeta.writerow(c)
    f.close()
def create():
    fh = open(r"userdet.csv")
    a = input("Enter the User ID to Search: ")
    userdet = csv.reader(fh)
    for j in userdet:
        l=list(j)        
        gg=len(j)
        while gg%10!=0:   
            g = l[0]
            k = l[1]
            gg-=1
    if g == a:
        print("The User With Id:",a,", has Password:",k)
    else:
        print("The User Doesn't Exist")
            
    fh.close()
add()
create()
