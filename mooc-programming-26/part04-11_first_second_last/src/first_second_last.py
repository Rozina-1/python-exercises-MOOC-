def first_word(sentence):
    i=0
    while i<=len(sentence):
        if sentence[i]==" ":
            return sentence[0:i]
        i=i+1
def second_word(sentence):
    i=len(first_word(sentence))+2
    j=i
    while i<=len(sentence):
        if sentence[i]==" ":
            return sentence[j:i]
        i=i+1
def last_word(sentence):
        i=len(second_word(sentence))
        if i+2<=len(sentence):
            i=len(sentence)-1
            while sentence[i]!=" ":
                i=i-1
            return sentence[i+1:]
if __name__ == "__main__":
    sentence = "first second"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))