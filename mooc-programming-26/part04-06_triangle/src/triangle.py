def line(num, string):
            print(string*num)
def triangle(size):
    i=1
    while i<=size:
        line(i, "#")
        i=i+1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
