def no_shouting(my_list):
    new = []
    for item in my_list:
        if item.isupper():
            continue
        else:
            new.append(item)
    return new
if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)
