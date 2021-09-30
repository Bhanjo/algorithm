def myCode():
    start = 1
    circle = 1
    num = int(input())
    i = 0
    while(True):
        circle = circle + (i*6)
        if(num <= circle and num >= start):
            print(i + 1)
            break
        else:
            i += 1
            start = circle

def main():
    myCode()
if __name__ == "__main__":
    main()