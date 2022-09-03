from collections import deque
import sys
input = sys.stdin.readline

dx = [-2, -2, -1, 1, 2, 2, 1, -1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]

tc = int(input())
for t in range(tc):
    n = int(input())
    graph = [[10**8]*n for _ in range(n)]
    q = deque()

    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    graph[start[0]][start[1]] = 0
    q.append([start[0], start[1], 0])

    while(q):
        x, y, cnt = q.popleft()
        for m in range(8):
            mx, my = dx[m] + x, dy[m] + y
            if 0 <= mx < n and 0 <= my < n:
                if graph[mx][my] > graph[x][y] + 1:
                    graph[mx][my] = graph[x][y] + 1
                    q.append([mx,my,cnt+1])
    print(graph[end[0]][end[1]])
    