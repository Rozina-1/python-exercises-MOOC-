def factorials(n):
    fact = {}
    for i in range(1,n+1):
        fact[i] = 1
        for j in range(1,i+1):
            fact[i] *= j
    return fact

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])