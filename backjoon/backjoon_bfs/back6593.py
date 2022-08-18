from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
graph = []
visit = [[False]*C for _ in range(R)]
answer = [0,0]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(R):
    col = list(input().strip())
    graph.append(col)

def bfs(i,j):
    q = deque()
    q.append([i,j])
    visit[i][j] = True
    sheep, wolf = 0,0
    while(q):
        x, y = q.popleft()
        if graph[x][y] == 'o':
            sheep += 1
        elif graph[x][y] == 'v':
            wolf += 1
        for i in range(4):
            mx, my = x + dx[i], y + dy[i]
            if 0 <= mx < R and 0 <= my < C:
                if not graph[mx][my] == '#' and not visit[mx][my]:
                    visit[mx][my] = True
                    q.append([mx,my])
    if sheep > wolf:
        answer[0] += sheep
    else:
        answer[1] += wolf

for i in range(R):
    for j in range(C):
        if (graph[i][j] == 'v' or graph[i][j] == 'o') and not visit[i][j]:
            bfs(i,j)

print(*answer)