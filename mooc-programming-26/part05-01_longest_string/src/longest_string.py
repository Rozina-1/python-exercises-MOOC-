def longest(mylist):
    i=0
    long = ""
    for item in mylist:
        if len(mylist[i])>len(long):
            long = mylist[i]
        i+=1
    return long
if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))