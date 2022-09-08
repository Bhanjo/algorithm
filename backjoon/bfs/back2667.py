from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(input().strip()) for _ in range(n)]
visit = [[False]*n for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = []
house = 0

def bfs(arr):
    q = deque()
    q.append([arr[0], arr[1]])
    visit[arr[0]][arr[1]] = True
    cnt = 0
    while(q):
        x,y = q.popleft()
        cnt += 1
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if 0 <= mx < n and 0 <= my < n:
                if visit[mx][my]: continue
                if graph[mx][my] == '1':
                    visit[mx][my] = True
                    q.append([mx,my])
    return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j] == '1' and not visit[i][j]:
            house += 1
            answer.append(bfs([i,j]))

answer.sort()
print(house)
for i in answer:
    print(i)