def largest():
    with open("numbers.txt") as new_file:
        greatest = 0
        for line in new_file:
            number1 = int(line.replace("\n",""))
            if number1 > greatest:
                greatest = number1
    return greatest
if __name__ == "__main__":
    largest()
