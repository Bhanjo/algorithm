import sys
input = sys.stdin.readline

n = int(input())
graph = []
visit = [[0]*n for _ in range(n)]
pos = [[-1,0], [1,0], [0,-1], [0,1]]
house = 0

for i in range(n):
    garo = list(map(int, input().strip()))
    graph.append(garo)

def dfs(x, y):
    if(x < 0 or x >= n or y < 0 or y >= n):
        return
    if(graph[x][y] != 1):
        return
    if(visit[x][y] == 0):
        visit[x][y] = 1
        global house
        house += 1

        for i in pos:
            dfs(x + i[0], y + i[1])

cnt = 0
ans = []
while(visit != graph):
    for i in range(n):
        for j in range(n):
            if(visit[i][j] == 0 and graph[i][j] == 1):
                house = 0
                dfs(i, j)
                ans.append(house)
                cnt += 1

print(cnt)
ans.sort()
for i in ans:
    print(i)