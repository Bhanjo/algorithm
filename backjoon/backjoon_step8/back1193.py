def myCode():
    num = int(input())
    i = 1
    while(num > i):
        num -= i
        i += 1
    if(i % 2 == 0):
        left = num
        right = i - num + 1
    else:
        left = i - num + 1
        right = num
    print("%d/%d"%(left,right))

def main():
    myCode()
if __name__ == "__main__":
    main()