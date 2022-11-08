import csv
def csvfile():
    f=open(r"C:\Users\User\Documents\student.csv","w")
    studdet=csv.writer(f)
    head=(["Roll.No","Name","Marks"])
    studdet.writerow(head)
    for i in range(1):
        print("Student Detail",(i+1))
        r=int(input("Enter the Roll Number: "))
        n=input("Enter the Name: ")
        m=int(input("Enter the Marks: "))
        studrec=([r,n,m])
        studdet.writerow(studrec)
    f.close()
    fh=open(r"C:\Users\User\Documents\student.csv","r",newline="")
    studred=csv.reader(fh)
    for j in studred:
        print(j)
    fh.close()
csvfile()
