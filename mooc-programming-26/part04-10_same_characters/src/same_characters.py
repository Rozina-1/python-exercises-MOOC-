def same_chars(string, i, j):
    num=len(string)
    if i < num and j < num:
         if string[i] == string[j]:
            return True
         else:
             return False
    else:
        return False

if __name__ == "__main__":
    print(same_chars("coder", 1, 2))