from collections import deque
import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())
graph = [[0]*m for _ in range(n)]
visit = [[False]*m for _ in range(n)]
answer = 0

for i in range(k):
    x,y = map(int, input().split())
    graph[x-1][y-1] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j):
    global answer
    cnt = 1
    q = deque()
    q.append([i,j])
    visit[i][j] = True

    while(q):
        x,y = q.popleft()
        for p in range(4):
            mx,my = x+dx[p], y+dy[p]
            if 0 <= mx < n and 0 <= my < m and not visit[mx][my]:
                if graph[mx][my] == 1:
                    visit[mx][my] = True
                    cnt += 1
                    q.append([mx,my])

    answer = max(answer, cnt)

for i in range(n):
    for j in range(m):
        if not visit[i][j] and graph[i][j] == 1:
            bfs(i,j)
    
print(answer)