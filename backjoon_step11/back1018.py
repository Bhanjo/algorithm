def myCode():
    x, y = map(int, input().split())
    ches = []
    mini = []

    for _ in range(x):
        ches.append(input())


    # 처음이 w일때, b일때 나눔
    for a in range(x-7):
        for b in range(y-7):
            cnt1 = 0 # 처음이 w일때 판별
            cnt2 = 0 # 처음이 b일때 판별
            for i in range(a, a+8):
                for j in range(b, b+8):
                    if(i + j) % 2 == 0:
                        if(ches[i][j] != 'W') : cnt1 += 1 # w가 아니면 처음이 w가 아닌게 됨(+1)
                        if(ches[i][j] != 'B') : cnt2 += 1
                    else :
                        if(ches[i][j] != 'B') : cnt1 += 1
                        if(ches[i][j] != 'W') : cnt2 += 1
            mini.append(cnt1)
            mini.append(cnt2)
    print(min(mini))



def main():
    myCode()
if __name__ == '__main__':
    main()