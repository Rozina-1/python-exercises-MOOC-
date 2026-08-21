def list_sum(a,b):
    i=0
    for item in a:
        a[i]=a[i]+b[i]
        i=i+1
    return a
if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) 