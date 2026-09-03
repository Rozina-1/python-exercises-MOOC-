def pbook():
    while True:
        choice = int(input("command (1 search, 2 add, 3 quit):"))
        if choice == 1:
            search()
        elif choice == 2:
            add()
        else:
            print("quitting...")
            return 0

def search():
    name = input("name: ")
    if name in phonebook:
        print(phonebook[name])
    else:
        print("no number")

def add():
    name = input("name: ")
    number = input("number: ")
    phonebook[name] = number
    print("ok!")

phonebook = {}
pbook()