def solution(brown, yellow):
    answer = []
    yellowNums = []
    
    # 약수 구하기
    for i in range(1, int(yellow**(1/2)) + 1):
        if yellow % i == 0:
            yellowNums.append(i)
            if i**2 != yellow:
                yellowNums.append(yellow // i)
    yellowNums.sort()
    
    # 노란색 크기 구하기 (가로 >= 세로)
    x = len(yellowNums) - 1
    y = 0
    while(x >= y):
        print(x,y,"디버그", ((yellowNums[x]+2)*2) + (yellowNums[y]*2))
        if (((yellowNums[x]+2)*2) + (yellowNums[y]*2)) == brown:
            answer.append(yellowNums[x]+2)
            answer.append(yellowNums[y]+2)
            break
        x -= 1
        y += 1
    print(answer)
    return answer
solution(24, 24)