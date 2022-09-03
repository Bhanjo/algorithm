import sys
sys.setrecursionlimit(1000001)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
visit = [[False]*m for _ in range(n)]
answer = 'NO'

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(arr):
    global answer
    if arr[0] == n-1:
        if graph[arr[0]][arr[1]] == '0':
            answer = 'YES'
        return
    for i in range(4):
        mx = arr[0] + dx[i]
        my = arr[1] + dy[i]
        if 0 <= mx < n and 0 <= my < m:
            if not visit[mx][my] and graph[mx][my] == '0':
                visit[mx][my] = True
                dfs([mx,my])

for i in range(len(graph[0])):
    if graph[0][i] == '0':
        visit[0][i] = True
        dfs([0,i])
        if answer == 'YES':
            break
print(answer)