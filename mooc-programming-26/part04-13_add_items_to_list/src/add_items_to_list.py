def add_items():
    num=int(input("How many itms: "))
    i=1
    list=[]
    while i<=num:
        item=int(input(f"Item {i}: "))
        list.append(item)
        i+=1
    print(list)
add_items()
