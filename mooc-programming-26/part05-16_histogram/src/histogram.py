def histogram(my_string):
    dict = {}
    for character in my_string:
        if character not in dict:
            dict[character] = ""
        dict[character] += "*"
    for key, value in dict.items():
        print(key + " " + value)

if __name__ == "__main__":
    histogram("statistically")