def distinct_numbers(my_list):
    unique_list = []
    
    for item in my_list:
        if item not in unique_list:
            unique_list.append(item)
            
    return sorted(unique_list)
if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list))  