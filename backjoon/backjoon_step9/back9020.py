def myCode():
    sosu = [0 for i in range(10001)]
    sosu[1] = 1
    for i in range(2, 98):
        for j in range(i * 2, 10001, i):
            sosu[j] = 1
    tc = int(input())
    for i in range(tc):
        num = int(input())
        nanum = num // 2
        for j in range(nanum, 1, -1): # 역순 nanum에서 1까지
            if(sosu[num - j] == 0 and sosu[j] == 0):
                print(j, num - j)
                break

def main():
    myCode()
if __name__ == '__main__':
    main()