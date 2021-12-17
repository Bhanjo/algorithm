import sys
input = sys.stdin.readline

n = int(input())
cardN = list(map(int, input().split()))
m = int(input())
cardM = list(map(int, input().split()))
isExist = []
cardN = sorted(cardN)

for i in cardM:
    low = 0
    higt = len(cardN) - 1
    while(True):
        mid = (low+higt) // 2
        if(i == cardN[mid]):
            isExist.append(1)
            break
        elif(low >= higt):
            isExist.append(0)
            break
        elif(i > cardN[mid]):
            low = mid + 1
        elif(i < cardN[mid]):
            higt = mid - 1

print(' '.join(map(str,isExist)))
