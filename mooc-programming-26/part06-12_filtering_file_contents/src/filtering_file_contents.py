def filter_solutions():
    incorrect = []
    correct = []
    with open("solutions.csv") as new_file:
        for line in new_file:
            line = line.strip("\n").split(";")
            if eval(line[1]) != int(line[2]):
                incorrect.append(f"{line[0]};{line[1]};{line[2]}")
            else:
                correct.append(f"{line[0]};{line[1]};{line[2]}")   

    with open("correct.csv","w") as new_file:
        for line in correct:
            new_file.write(line + "\n")

    with open("incorrect.csv","w") as new_file:
        for line in incorrect:
            new_file.write(line + "\n")

if __name__ == "__main__":
    filter_solutions()
        