def double_items(numbers):
    new_list = []
    for item in numbers:
        new_list.append(2*item)
    return new_list
if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)