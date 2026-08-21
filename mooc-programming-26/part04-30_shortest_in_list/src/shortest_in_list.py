def shortest(my_list):
    best = my_list[0]
    for item in my_list:
        if len(item)<len(best):
            best = item
    return best
if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)