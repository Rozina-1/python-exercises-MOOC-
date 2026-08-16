def same_word():
    list=[]
    i=0
    flag=0
    while True:
        word=input("Word: ")
        if word in list:
            break
        list.append(word)
    
    print(f"You typed in {len(list)} different words")
same_word()