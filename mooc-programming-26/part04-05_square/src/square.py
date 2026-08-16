# Copy here code of line function from previous exercise
def line(num, string):
            print(string*num)
def square(size, character):
    i=size
    while i>0:
        line(size, character)
        i=i-1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")