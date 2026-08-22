def no_vowels(str):
    vowel = "aeiou"
    for item in vowel:
            str = str.replace(item,"")
    return str
if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))


# def no_vowels(str):
#     str1 = str
#     for item in str1:
#         if item == "a" or item == "i" or item == "e" or item == "o" or item == "u":
#             str = str.replace(item,"")
#     return str
# if __name__ == "__main__":
#     my_string = "this is an example"
#     print(no_vowels(my_string))