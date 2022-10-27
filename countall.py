def countall():
    a = 0
    aa = 0
    ua = 0
    la = 0
    d = 0
    sc = 0
    s = 0
    f = open("C:\\Users\\navik\\Downloads\School\\test.txt")
    y = f.read()
    for i in y:
        if i!="":
            a += 1
        if i >= "A" and i <= "Z" or i >= "a" and i <= "z":
            aa += 1
        if i >= "A" and i <= "Z":
            ua += 1
        if i >= "a" and i <= "z":
            la += 1
        elif i >= "0" and i <= "9":
            d += 1
        elif i == " ":
            s += 1
        else :
            sc += 1
    print("Total Number of Characters: ", a)
    print("Total Number of Alphabets: ", aa)
    print("Total Number of Uppercase: ", ua)
    print("Total Number of Lowercase: ", la)
    print("Total Number of Digits: ", d)
    print("Total Number of Spaces: ", s)
    print("Total Number of Special Characters: ", sc)


countall()
