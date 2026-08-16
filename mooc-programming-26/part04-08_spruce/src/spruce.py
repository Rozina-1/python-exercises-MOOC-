# Write your solution here
def spruce(size):
    print("a spruce!")
    i=size
    j=0
    while i>0:
        print(" "*(i-1),end="")
        print("*"*(j+1))
        j=j+2
        i=i-1
    print(" "*(size-1),end="*")
if __name__ == "__main__":
    spruce(5)