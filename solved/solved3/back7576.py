import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
posX = [-1,1,0,0]
posY = [0,0,-1,1]
graph = []
q = deque()

for sero in range(N):
    temp = list(map(int, input().split()))
    graph.append(temp)
    for garo in range(M):
        if(graph[sero][garo] == 1):
            q.append([sero,garo])

while(q):
    x, y = q.popleft()
    for i in range(len(posX)):
        moveX = x + posX[i]
        moveY = y + posY[i]
        if(0 <= moveX < N and 0 <= moveY < M and graph[moveX][moveY] == 0):
            q.append([moveX, moveY])
            graph[moveX][moveY] = graph[x][y] + 1

ans = 0
for i in range(N):
    for j in range(M):
        if(graph[i][j] == 0):
            print(-1)
            exit(0)
    ans = max(ans, max(graph[i]))
print(ans - 1)