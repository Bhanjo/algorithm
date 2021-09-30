def myCode():
    num = int(input())
    i = 2
    while(True):
        if(num == 1):
            break
        else:
            if(num % i == 0):
                print(i)
                num = num / i
            else:
                i += 1

def main():
    myCode()
if __name__ == '__main__':
    main()