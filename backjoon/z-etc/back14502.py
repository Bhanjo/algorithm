from collections import deque
import copy
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = 0

# 3개의 벽 추가 생성
def makeWall(cnt):
    if cnt == 3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(cnt+1)
                graph[i][j] = 0

def bfs():
    global ans
    q = deque()
    copyGraph = copy.deepcopy(graph) # 그래프 원본 유지를 위해 깊은 복사
    
    # 바이러스 시작점 찾기
    for i in range(n):
        for j in range(m):
            if copyGraph[i][j] == 2:
                q.append((i,j))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            px = dx[i]+x
            py = dy[i]+y
            if 0 <= px < n and 0 <= py < m: # 그래프 내에 움직일 수 있는 위치인지 판별
                if copyGraph[px][py] == 0:
                    copyGraph[px][py] = 2
                    q.append((px,py))
    
    cntZero = 0
    for i in copyGraph:
        cntZero += i.count(0)
    ans = max(ans, cntZero)

makeWall(0)
print(ans)