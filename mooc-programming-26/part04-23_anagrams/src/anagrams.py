def anagrams(str1,str2):
    if(sorted(str1)==sorted(str2)):
        return True
    else:
        return False

if __name__ == "__main__":
    str1 = input("Enter a string: ")
    str2 = input("Ener another string: ")
    print(anagrams(str1,str2))