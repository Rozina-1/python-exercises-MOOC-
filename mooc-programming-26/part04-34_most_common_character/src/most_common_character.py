def most_common_character(str):
    temp = 0
    st = ""
    for item in str:
        if str.count(item)>temp:
            temp=str.count(item)
            st=item
    return st
if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))