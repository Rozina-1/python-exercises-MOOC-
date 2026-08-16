def range_of_list(my_list):
    num=sorted(my_list)
    return (num[len(my_list)-1]-num[0])
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print("The range of the list is:",result)