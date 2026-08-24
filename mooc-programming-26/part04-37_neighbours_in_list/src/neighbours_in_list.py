def longest_series_of_neighbours(my_list):
    count = 0
    val = 0
    
    for i in range(len(my_list) - 1):
        if my_list[i] - my_list[i+1] == 1 or my_list[i] - my_list[i+1] == -1:
            count = count + 1
        else:
            if count > val:
                val = count
            count = 0
    val = max(val, count)
    return val + 1 if val > 0 else 1
if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))  

