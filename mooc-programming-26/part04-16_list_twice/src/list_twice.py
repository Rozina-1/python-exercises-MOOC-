def list_twice():
    list=[]
    while True:
        item=int(input("New item: "))
        list.append(item)
        if item==0:
            break
        print(f"The list now: {list}")
        print(f"The list in order: {sorted(list)}")
    print("Bye!")
list_twice()