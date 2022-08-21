import sys
input = sys.stdin.readline

N, M = map(int, input().split())
temp = []

def dfs(num):
    if len(temp) == M:
        print(*temp)
        return
    for i in range(num, N+1):
        temp.append(i)
        dfs(i)
        temp.pop()

dfs(1)