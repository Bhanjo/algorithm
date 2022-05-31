from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = []
visit = [[0]*n for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
q = []
check = False
cnt1 = 0
cnt2 = 0
target = ''

for i in range(n):
    row = list(input().strip())
    graph.append(row)

def bfs():
    global cnt1, cnt2
    while(q):
        curr = q.pop()
        currX, currY = curr[0], curr[1]
        if visit[currX][currY] == 0:
            visit[currX][currY] = 1
            for i in range(4):
                if 0 <= currX + dx[i] < n and 0 <= currY + dy[i] < n:
                    if target == graph[currX + dx[i]][currY + dy[i]] or (check == True and (target == 'R' or target =='G') and (graph[currX + dx[i]][currY + dy[i]] == 'R' or graph[currX + dx[i]][currY + dy[i]] == 'G')):
                        q.append([currX + dx[i], currY + dy[i]])
    if not check:
        cnt1 += 1
    else:
        cnt2 += 1


for col in range(n):
    for row in range(n):
        if visit[col][row] == 0:
            q.append([col,row])
            target = graph[col][row]
            bfs()

visit = [[0]*n for _ in range(n)]
check = True
for col in range(n):
    for row in range(n):
        if visit[col][row] == 0:
            q.append([col,row])
            target = graph[col][row]
            bfs()

print(cnt1, cnt2)