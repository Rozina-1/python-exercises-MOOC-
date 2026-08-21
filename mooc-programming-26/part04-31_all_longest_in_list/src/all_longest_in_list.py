def all_the_longest(my_list):
    longest_words = []
    max_len = 0
    
    for item in my_list:
        current_len = len(item)
        
        if current_len > max_len:
            max_len = current_len
            longest_words = [item]
            
        elif current_len == max_len and max_len > 0:
            longest_words.append(item)
            
    return longest_words
if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']