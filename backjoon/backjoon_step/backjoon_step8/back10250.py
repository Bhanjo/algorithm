def myCode():
    tc = int(input())
    for i in range(tc):
        # h: 층, w: 방, n: n번째 손님
        h, w, n = map(int,input().split())

        if(int(n % h) == 0):
            garo = int(n / h)
            sero = h
        else:
            garo = int(n / h) + 1
            sero = int(n % h)

        print((sero*100)+garo) 

def main():
    myCode()
if __name__ == '__main__':
    main()