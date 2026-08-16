# Write your solution here
# You can test your function by calling it within the following block
def mean(my_list):
    i=0
    num=0
    while (i!=len(my_list)):
        num+=my_list[i]
        i=i+1
    return num/len(my_list)
    
if __name__ == "__main__":
    my_list = [3, 6, 3]
    result = mean(my_list)
    print("Mean is ",result)