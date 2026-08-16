list=[]
i=1
while True:
    print(f"The list is now {list}")
    op = input("a(d)d, (r)remove or e(x)it: ")
    if op== 'd':
        list.insert(len(list),i)
        i=i+1
    elif op=='r':
        list.remove(i-1)
        i=i-1
    else :
        break
print("Bye!")