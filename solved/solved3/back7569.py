import sys
from collections import deque
input = sys.stdin.readline

M,N,H = map(int, input().split())
graph = []
q = deque()
for h in range(H):
    box = []
    for n in range(N):
        garo = list(map(int, input().split()))
        box.append(garo)
        # 토마토 위치 찾아 넣기
        for m in range(M):
            if box[n][m] == 1:
                q.append([h,n,m])
    graph.append(box)

posX = [-1, 1, 0, 0, 0, 0]
posY = [0, 0, -1, 1, 0, 0]
posZ = [0, 0, 0, 0, -1, 1]

while(q):
    z,x,y = q.popleft()
    for i in range(len(posX)):
        moveX = x + posX[i]
        moveY = y + posY[i]
        moveZ = z + posZ[i]
        if(0 <= moveX < N and 0 <= moveY < M and 0 <= moveZ < H):
            if(graph[moveZ][moveX][moveY] == 0):
                q.append([moveZ, moveX, moveY])
                graph[moveZ][moveX][moveY] = graph[z][x][y] + 1

ans = 0
for height in graph:
    for sero in height:
        for garo in sero:
            if garo == 0:
                print(-1)
                exit(0)
        ans = max(ans, max(sero))
print(ans - 1)