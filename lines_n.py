def length():
    f = open("C:\\Users\\navik\\Downloads\\School\\Text.txt")
    for i, l in enumerate(f):
        pass
    return i+1


def text():
    f = open("C:\\Users\\navik\\Downloads\\School\\Text.txt")
    g = length()
    while g > 0:
        d=f.readline()
        p=[*d]
        h = len(p)-2
        l=len(p)-1
        hh=p[h]
        ll=p[l]
        if hh== "n" or ll=="n":
            print(d)
        else:
            pass
        g -= 1
    f.close()


text()
