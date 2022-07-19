from collections import deque
import sys
input = sys.stdin.readline

# 위 아래 왼 오 왼위 오위 왼아 오아
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def dfs(q, graph, visit):
    while(q):
        i, j = q.pop()
        if not visit[i][j]:
            visit[i][j] = True
            for d in range(8):
                mx, my = dx[d] + i, dy[d] + j
                if (0 <= mx < h and 0 <= my < w) and graph[mx][my] == 1:
                    q.append((mx,my))

# main
while(True):
    w, h = map(int, input().split())
    if w == h == 0:
        break

    answer = 0
    graph = [list(map(int, input().split())) for _ in range(h)]
    visit = [[False]*w for _ in range(h)]
    q = deque()
    
    for x in range(h):
        for y in range(w):
            if graph[x][y] == 1 and not visit[x][y]:
                q.append((x,y))
                dfs(q, graph, visit)
                answer += 1
    print(answer)