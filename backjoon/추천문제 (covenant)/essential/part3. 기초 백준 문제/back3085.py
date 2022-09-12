import sys
input = sys.stdin.readline

n = int(input())
graph = []
answer = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    graph.append(list(input()))

def findColumn(color, x, y): # 위, 아래 탐색
    up, down = x-1,x+1
    cnt = 1
    while(up >= 0 or down < n):
        if up >= 0:
            if graph[up][y] == color:
                cnt += 1
                up -= 1
            else:
                up = -1
        if down < n:
            if graph[down][y] == color:
                cnt += 1
                down += 1
            else:
                down = n
    return cnt

def findRow(color, x, y): # 좌, 우 탐색
    left, right = y-1, y+1
    cnt = 1
    while(left >= 0 or right < n):
        if left >= 0:
            if graph[x][left] == color:
                cnt += 1
                left -= 1
            else:
                left = -1
        if right < n:
            if graph[x][right] == color:
                cnt += 1
                right += 1
            else:
                right = n
    return cnt

for i in range(n):
    for j in range(n):
        # 바꾸지 않고 실행
        col = findColumn(graph[i][j],i,j)
        row = findRow(graph[i][j],i,j)
        answer = max(answer, col, row)
        for m in range(4):
            mx,my = i+dx[m], j+dy[m]
            if 0 <= mx < n and 0 <= my < n:
                # 위치 바꾸기, 바꾼 후 원상복구 필요
                if graph[mx][my] != graph[i][j]:
                    # 행 열 바꾸고 다시 실행
                    graph[i][j], graph[mx][my] = graph[mx][my], graph[i][j]
                    col = findColumn(graph[i][j],i,j)
                    row = findRow(graph[i][j],i,j)
                    answer = max(answer, col, row)
                    # 서로 바꿨던 것을 원상복구
                    graph[mx][my], graph[i][j] = graph[i][j], graph[mx][my]

print(answer)