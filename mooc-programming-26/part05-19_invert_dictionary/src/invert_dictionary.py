def invert(d):
    dictorg = {}
    for key,item in d.items():
        dictorg[item] = key
    d.clear()
    for newkey, newitm in dictorg.items():
        d[newkey] = newitm

if __name__ == "__main__":       
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)