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
    fh = open(r"userdet.csv",newline='\r\n')
    a = input("Enter the User ID to Search: ")
    userdet = csv.reader(fh)
    for j in userdet:  
        g = j[0]
        k = j[1]
    if g == a:
        print()
        print("The User With Id:",a,", has Password:",k)
    else:
        print()
        print("The User Doesn't Exist")
            
    fh.close()
add()
create()
