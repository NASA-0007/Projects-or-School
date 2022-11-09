import csv
def menu():
    while True:
        a=print("1.Create CSV File")
        b=print("2.Search")
        c=print("3.Exit")
        print()
        ch=int(input("Enter a Choice: "))
        if ch==1:
            f=open("emp_det.csv","w")
            empdet=csv.writer(f)
            empdet.writerow(["Dept.ID","Name","City"])
            print()
            k=int(input("Number of Datas to be Added: "))
            print()
            
            for i in range(k):
                aa=input("Department Number: ")
                bb=input("Name: ")
                cc=input("City: ")
                print()
                dd=([aa,bb,cc])
                empdet.writerow(dd)
            f.close()
        elif ch==2:
            fh=open("emp_det.csv",newline='\r\n')
            print()
            kk=input("Enter the Department ID to be Searched: ")
            empread=csv.reader(fh)
            got=False
            for j in empread:
                g = j[0]
                k = j[1]
                h = j[2]
                if kk==g:
                    print()
                    print("Department ID:",g,"Name:",k,"City:",h)
                    print()
                    got=True
            if got==False:
                print()
                print("The Department ID doesn't Exist")
                print()
            fh.close()
        elif ch==3:
            break
        else:
            print("Enter a Valid Input")
menu()
