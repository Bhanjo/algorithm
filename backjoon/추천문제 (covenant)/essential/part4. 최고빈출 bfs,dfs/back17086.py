from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

def bfs(node):
    q = deque()
    q.append(node)
    visit = [[0]*m for _ in range(n)]

    while(q):
        x,y = q.popleft()
        if graph[x][y] == 1:
            return visit[x][y]
        for i in range(8):
            mx, my = x+dx[i], y+dy[i]
            if 0 <= mx < n and 0 <= my < m:
                if visit[mx][my] != 0: continue
                visit[mx][my] = visit[x][y] + 1
                q.append([mx,my])
    
answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            answer = max(answer, bfs([i,j]))

print(answer)