def list_of_stars(my_list):
    i = 0
    while i < len(my_list):
        print("*" * my_list[i])
        i = i + 1


if __name__ == "__main__":
    list_of_stars([3, 7, 10])