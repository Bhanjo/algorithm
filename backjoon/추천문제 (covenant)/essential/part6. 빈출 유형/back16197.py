from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
coins = []
answer = -1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 코인 초기 위치 찾기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'o':
            coins.append([i,j])

def isOver(a,b):
    # a는 떨어졌고 b는 산 경우
    if not (0 <= a[0] < n and 0 <= a[1] < m):
        if 0 <= b[0] < n and 0 <= b[1] < m:
            return True
    
    # b는 떨어졌고 a는 산 경우
    if not (0 <= b[0] < n and 0 <= b[1] < m):
        if 0 <= a[0] < n and 0 <= a[1] < m:
            return True
    
    # 둘 다 떨어지거나 둘 다 살아있으면 계속 진행
    return False

def bfs():
    global answer
    q = deque()
    q.append([coins, 0]) # [[코인,코인], 카운트]
    while(q):
        coin, cnt = q.popleft()
        if cnt >= 10: return
        coinA, coinB = coin
        for i in range(4):
            ax, ay = coinA[0] + dx[i], coinA[1] + dy[i]
            bx, by = coinB[0] + dx[i], coinB[1] + dy[i]
            if isOver([ax,ay],[bx,by]):
                answer = cnt + 1
                return
            if 0 <= ax < n and 0 <= ay < m and 0 <= bx < n and 0 <= by < m:
                if graph[ax][ay] != '#' and graph[bx][by] != '#':
                    q.append([[[ax,ay],[bx,by]],cnt+1])
                if graph[ax][ay] == '#' and graph[bx][by] != '#':
                    q.append([[coinA,[bx,by]],cnt+1])
                if graph[ax][ay] != '#' and graph[bx][by] == '#':
                    q.append([[[ax,ay],coinB],cnt+1])


bfs()
print(answer)