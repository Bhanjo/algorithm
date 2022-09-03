from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
maxHeight = -10**5
answer = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 그래프에 row 추가 및 최대 높이 구하기
graph = []
for i in range(n):
    garo = list(map(int, input().split()))
    maxHeight = max(maxHeight, max(garo))
    graph.append(garo)

# graph[i][j] == -1 일 때 물에 잠겼다는 뜻
for water in range(maxHeight):
    visit = [[False]*n for _ in range(n)]
    q = deque()
    cnt = 0

    # bfs 수행
    for i in range(n):
        for j in range(n):
            if graph[i][j] > water and not visit[i][j]:
                q.append((i,j))
                while(q):
                    x, y = q.popleft()
                    for m in range(4):
                        mx, my = dx[m] + x, dy[m] + y
                        if 0 <= mx < n and 0 <= my < n and not visit[mx][my]:
                            if graph[mx][my] > water:
                                visit[mx][my] = True
                                q.append((mx,my))
                cnt += 1
    answer = max(answer, cnt)

print(answer)
