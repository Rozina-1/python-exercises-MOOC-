def palindromes(str2):
    if(str2[::-1]==str2):
        return True
    else:
        return False
while(True):
    str1 = input("Please type in a palindrome: ")
    if(palindromes(str1)):
        print(str1,"is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")
