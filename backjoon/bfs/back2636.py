from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
hour = 0
lastCount = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(arr):
    visit = [[False]*m for _ in range(n)]
    visit[arr[0]][arr[1]] = True
    q = deque()
    q.append(arr)
    while(q):
        x,y = q.popleft()
        # 치즈면 해당 부분 녹이고 방문처리
        if graph[x][y] == 1:
            graph[x][y] = 0
            visit[x][y] = True
            continue # 치즈 녹인 부분에서 탐색을 하면 안쪽까지 들어가기 때문
        # 탐색
        for i in range(4):
            mx, my = x + dx[i], y + dy[i]
            if 0 <= mx < n and 0 <= my < m:
                if visit[mx][my]:
                    continue
                visit[mx][my] = True
                q.append([mx,my])

while(True):
    count = 0
    # 치즈 크기 구하고 끝났는지 판단
    for i in graph:
        for j in i:
            if j == 1:
                count += 1
    if count == 0:
        break
    else:
        lastCount = count
        bfs([0,0])
        hour += 1

print(hour, lastCount)