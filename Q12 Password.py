import csv
def add():
    f = open(r"C:\Users\navik\Downloads\School\userdet.csv", "w")
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
        f.flush()
    f.close()
def create():
    fh = open(r"C:\Users\navik\Downloads\School\userdet.csv")
    a = input("Enter the User ID to Search: ")
    userdet = csv.reader(fh)
    for j in userdet:
        gg=len(j)
        while gg%10!=0:   
            g = j[0]
            k = j[1]
            gg+=1
    if g == a:
        print("The User With Id:",a,", has Password:",k)
    else:
        pass
            
    fh.close()
add()
create()
