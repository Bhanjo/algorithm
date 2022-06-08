import sys
input = sys.stdin.readline

n = int(input())
houses = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(3):
        houses[i][j] = min(houses[i-1][j-1] + houses[i][j], houses[i-1][j-2] + houses[i][j])
print(min(houses[n-1]))