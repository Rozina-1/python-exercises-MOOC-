def main():
    phonebook = {}
    while True:
        choice =input("command (1 search, 2 add, 3 quit):")
        if choice == "1":
            search(phonebook)
        elif choice == "2":
            add(phonebook)
        else:
            print("quitting...")
            break

def search(phonebook):
    name = input("name: ")
    if name in phonebook:
        for number in phonebook[name]:
            print(number)
    else:
        print("no number")

def add(phonebook):
    name = input("name: ")
    number = input("number: ")
    if name not in phonebook:
        phonebook[name] = []
    phonebook[name].append(number)
    print("ok!")

main()