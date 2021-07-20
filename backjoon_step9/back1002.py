def myCode():
    tc = int(input())
    for _ in range(tc):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        r = ((x2 - x1)**2 + (y2 - y1)**2) ** (1/2)
        rhap = r1+r2
        rcha = abs(r1 - r2)
        if r == 0:
            if(r1 == r2):
                print(-1)
            else:
                print(0)
        else:
            if(r == rhap or r == rcha):
                print(1)
            elif(r < rhap and r > rcha):
                print(2)
            else:
                print(0)

def main():
    myCode()
if __name__ == '__main__':
    main()