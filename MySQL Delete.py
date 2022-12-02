import mysql.connector as sql
a=sql.connect(host='localhost',user='root',passwd='computer')
cur=a.cursor()
cur.execute("drop database stud_det;")
cur.execute("create database stud_det;")
a=sql.connect(host='localhost',user='root',passwd='computer',database='stud_det')
cur=a.cursor()
cur.execute('create table student(Roll_no int,Name varchar(20),Class varchar(5));')
def display():
    a=sql.connect(host='localhost',user='root',passwd='computer',database='stud_det')
    cur=a.cursor()
    cur.execute('select * from student;')
    print(cur.fetchall())
def insert():
    a=sql.connect(host='localhost',user='root',passwd='computer',database='stud_det')
    cur=a.cursor()
    r=int(input("Enter the Roll No: "))
    n=input("Enter the Name: ")
    c=input("Enter the Class: ")
    val="insert into student values({},'{}','{}')".format(r,n,c);
    cur.execute(val)
    a.commit()
def delete():
    a=sql.connect(host='localhost',user='root',passwd='computer',database='stud_det')
    cur=a.cursor()
    n=int(input('Enter the roll no of student to be deleted :'))
    cur.execute("delete from student where Roll_no="+str(n))
    a.commit()
def menu():
    while True:
        print("1:Insert")
        print("2:Display")
        print("3:Delete")
        print("4:Exit")
        ch=int(input("Enter your Choice"))
        if ch==1:
            insert()
        elif ch==2:
            display()
        elif ch==3:
            delete()
        elif ch==4:
            break
        else:
            print("Enter a Valid Input")
menu()
