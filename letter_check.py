def length():
    f = open("C:\\Users\\navik\\Downloads\\School\\Text.txt")
    for i,l in enumerate(f):
        pass
    return i+1


def counta():
    f = open("C:\\Users\\navik\\Downloads\\School\\Text.txt")
    a = 0
    l = length()
    while l > 0:
        b = f.read(1)
        if b == "a":
            a += 1
        elif b == "A":
            a += 1
        l -= 1
    print("Total Number of line starting with a or A is:", a)
    f.close()


counta()
