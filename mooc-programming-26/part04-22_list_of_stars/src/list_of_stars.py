def list_of_stars():
    # .split() takes user input like "3 1 5" and turns it into a list: ['3', '1', '5']
    my_list = input("Please enter numbers separated by space: ").split()

    i = 0
    while i < len(my_list):
        num = int(my_list[i])  
        print("*" *num)
        i = i + 1


list_of_stars()