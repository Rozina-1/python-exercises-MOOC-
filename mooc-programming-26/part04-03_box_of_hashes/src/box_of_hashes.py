# Copy here code of line function from previous exercise

def box_of_hashes(height):
    # You should call function line here with proper parameters
    while height>0:
        def line(num, string):
            print(string*num)
        line(10, "#")
        height=height-1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
