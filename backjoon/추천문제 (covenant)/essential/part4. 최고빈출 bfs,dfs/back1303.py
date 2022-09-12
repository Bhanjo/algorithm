from collections import deque
import sys
input = sys.stdin.readline

m,n = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
visit = [[False]*m for _ in range(n)]
w,b = 0,0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(color,i,j):
    global w
    global b
    cnt = 1
    q = deque()
    q.append([i,j])
    visit[i][j] = True
    while(q):
        x,y = q.popleft()
        for k in range(4):
            mx = x+dx[k]
            my = y+dy[k]
            if 0 <= mx < n and 0 <= my < m:
                if not visit[mx][my] and graph[mx][my] == color:
                    visit[mx][my] = True
                    cnt += 1
                    q.append([mx,my])
        
    if color == 'W':
        w += cnt**2
    else:
        b += cnt**2

for i in range(n):
    for j in range(m):
        if not visit[i][j]:
            bfs(graph[i][j],i,j)
            
print(w,b)