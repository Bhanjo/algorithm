from collections import deque
import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = 0

def bfs(x,y):
    q = deque()
    q.append([x,y])
    union = [[x,y]]

    while(q):
        x, y = q.popleft()
        for i in range(4):
            mx = dx[i] + x
            my = dy[i] + y
            if 0 <= mx < N and 0 <= my < N:
                if visit[mx][my] == 0 and L <= abs(graph[x][y] - graph[mx][my]) <= R:
                    visit[mx][my] = 1
                    q.append([mx,my])
                    union.append([mx,my])
    
    return union

while(True):
    visit = [[0] * N for _ in range(N)]
    isExist = False
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
                visit[i][j] = 1
                union = bfs(i,j)
                if len(union) >= 2:
                    isExist = True
                    hap = 0
                    for u in union:
                        hap += graph[u[0]][u[1]]
                    for u in union:
                        graph[u[0]][u[1]] = hap // len(union)
    if not isExist:
        break
    answer += 1

print(answer)