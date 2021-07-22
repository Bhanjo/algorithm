def fibo(num):
    if(num == 0):
        return 0
    elif(num == 1):
        return 1
    else:
        return fibo(num-1) + fibo(num-2)

def myCode():
    num = int(input())
    print(fibo(num))

def main():
    myCode()
    
if __name__ == '__main__':
    main()