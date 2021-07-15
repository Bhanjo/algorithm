def filter(n):
    if(n <= 1):
        return 0
    if(n == 2):
        return 2
    i = 2
    while(i*i <= n):
        if(n % i*i == 0):
            return 0
        i += 1
    return n

def myCode():
    num1 = int(input())
    num2 = int(input())
    sosu = []
    for i in range(num1, num2 + 1):
        if(filter(i) > 0):
            sosu.append(filter(i))
    if(sosu):
        print(sum(sosu))
        print(min(sosu))
    else:
        print(-1)



def main():
    myCode()
if __name__ == '__main__':
    main()