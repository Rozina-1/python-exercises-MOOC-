def line(num, string):
            print(string*num)
def shape(width, triS, rectH, rectS):
        i=1
        while i<=width:
                line(i, triS)
                i=i+1
        i=1
        while i<=rectH:
                line(width,rectS)
                i+=1
if __name__ == "__main__":
    shape(5, "x", 2, "o")