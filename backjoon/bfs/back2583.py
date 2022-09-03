from collections import deque
import sys
input = sys.stdin.readline

N,M,K = map(int, input().split())
graph = [[0]*M for _ in range(N)]
visit =[[0]*M for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

total = 0
area = []

for t in range(K):
    Ax, Ay, Bx, By = map(int, input().split())
    for i in range(Ay, By):
        for j in range(Ax, Bx):
            graph[i][j] = 1
            visit[i][j] = 1

def bfs(i,j):
    q = deque()
    q.append([i,j])
    visit[i][j] = 1
    currArea = 1

    while(q):
        x, y = q.popleft()
        for i in range(4):
            mx = dx[i] + x
            my = dy[i] + y
            if 0 <= mx < N and 0 <= my < M:
                if graph[mx][my] == 0:
                    if visit[mx][my] == 0:
                        visit[mx][my] = 1
                        currArea += 1
                        q.append([mx,my])
    area.append(currArea)

for i in range(N):
    for j in range(M):
        if visit[i][j] == 0:
            total += 1
            bfs(i,j)

print(total)
area.sort()
print(*area)