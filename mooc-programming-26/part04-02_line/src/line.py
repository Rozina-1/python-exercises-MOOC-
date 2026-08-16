# Write your solution here
# You can test your function by calling it within the following block
def line(num, string):
    if string=="":
        string="*"
    while num>0:
        print(string[0],end="")
        num=num-1
if __name__ == "__main__":
    line(5, "")