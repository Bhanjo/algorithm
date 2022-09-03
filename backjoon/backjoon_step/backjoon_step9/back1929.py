def sosu(num):
    if(num <= 1):
        return
    else:
        for i in range(2, int(num**(1/2))+1):
            if(num % i == 0):
                return
        return num

def myCode():
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        if(sosu(i)):
            print(i)

def main():
    myCode()
if __name__ == '__main__':
    main()