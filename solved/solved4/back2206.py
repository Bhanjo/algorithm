from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]

# 3차원 배열, [가로][세로][파괴여부]
visit = [[[0]*2 for _ in range(m)] for _ in range(n)]
visit[0][0][0] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

answer = -1

def bfs(i,j,k):
    global answer
    q = deque()
    q.append([i,j,k])
    while(q):
        x,y,c = q.popleft()
        if x == n-1 and y == m-1:
            answer = visit[x][y][c]
            break
        for d in range(4):
            mx = dx[d] + x
            my = dy[d] + y
            # 갈 수 있음
            if 0 <= mx < n and 0 <= my < m:
                # 길 만남, 아직 방문 안함
                if graph[mx][my] == '0' and visit[mx][my][c] == 0:
                    q.append([mx,my,c])
                    visit[mx][my][c] = visit[x][y][c] + 1
                elif graph[mx][my] == '1' and c == 0:
                    # 벽 만남, 벽 파괴 가능
                    q.append([mx,my,1])
                    visit[mx][my][1] = visit[x][y][0] + 1

bfs(0,0,0)
print(answer)