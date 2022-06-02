import sys
input = sys.stdin.readline

answer = -100000000
n, m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visit = [[False]*m for _ in range(n)]
move = [(1,0), (-1,0), (0,-1), (0,1)]

# ㅡ, ㅁ, L, ㄴㄱ 테트로미노 계산
def dfs(x, y, value, cnt):
    global answer
    if cnt == 4: # 테트리스 방향 다 탐색
        answer = max(answer, value)
        return
    
    # 현 위치에서 4방향 탐색, 갈 수 있다면 dfs 실행
    for i in range(4):
        moveX = x + move[i][0]
        moveY = y + move[i][1]
        if 0 <= moveX < n and 0 <= moveY < m and not visit[moveX][moveY]:
            visit[moveX][moveY] = True
            dfs(moveX, moveY, value + graph[moveX][moveY], cnt + 1)
            visit[moveX][moveY] = False

# ㅗ모양 탐색
def checkMountain(x, y):
    global answer
    for i in range(4):
        value = graph[x][y]
        for k in range(3):
            # move 배열에 있는 튜플을 각각 3번만 사용하기
            tp = (i + k) % 4
            moveX = x + move[tp][0]
            moveY = y + move[tp][1]
            if not (0 <= moveX < n and 0 <= moveY < m):
                value = 0
                break
            value += graph[moveX][moveY]
        answer = max(answer, value)

for i in range(n):
    for j in range(m):
        visit[i][j] = True
        dfs(i,j, graph[i][j], 1)
        visit[i][j] = False
        checkMountain(i, j)

print(answer)