from collections import deque
import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]
n = int(input())
graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(n):
        if row[j] == 9: # 상어가 있는 위치를 2(상어 기본 lv)로 변경
            graph[i][j] = 2
            start = [i,j]

def bfs(i, j):
    visit = [[0] * n for _ in range(n)]
    visit[i][j] = 1
    eat = []
    dist = [[0] * n for _ in range(n)]
    q = deque()
    q.append((i,j))

    while(q):
        x, y = q.popleft()
        for k in range(4):
            posX = x + dx[k]
            posY = y + dy[k]
            if 0 <= posX < n and 0 <= posY < n:
                if visit[posX][posY] == 0:
                    # 지나갈 수 있을 때
                    if graph[posX][posY] <= graph[i][j] or graph[posX][posY] == 0:
                        visit[posX][posY] = 1
                        q.append((posX, posY))
                        dist[posX][posY] = dist[x][y] + 1 # 거리 갱신
                    if graph[posX][posY] < graph[i][j] and graph[posX][posY] != 0:
                        eat.append([posX, posY, dist[posX][posY]]) # 먹을 수 있다면 먹기
    if not eat: # 먹은게 없다면 리턴
        return -1, -1, -1
    eat.sort(key = lambda x : (x[2],x[0],x[1]))
    return eat[0][0], eat[0][1], eat[0][2]

exp = 0
cnt = 0

while(True):
    i, j = start[0], start[1]
    ex, ey, dist = bfs(i,j) # 시작점을 기준으로 bfs 실행
    if ex == -1: # 먹은것이 없다면 종료
        break
    graph[ex][ey] = graph[i][j] # 최종적으로 먹은 곳에 상어 이동시키기
    graph[i][j] = 0
    start = [ex, ey]
    exp += 1
    if exp == graph[ex][ey]: # lv 올릴 수 있으면 올리기
        exp = 0
        graph[ex][ey] += 1
    cnt += dist

print(cnt)