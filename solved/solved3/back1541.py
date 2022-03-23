import sys
input = sys.stdin.readline

words = input().strip().split('-')
toNums = []
for i in words:
    hap = 0
    plus = i.split('+')
    for j in plus:
        hap += int(j)
    toNums.append(hap)
ans = toNums[0]
for i in range(1, len(toNums)):
    ans -= toNums[i]
print(ans)