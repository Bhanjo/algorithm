from collections import deque
import sys
input = sys.stdin.readline

garo = 6
sero = 12
graph = [list(input().strip()) for _ in range(sero)]
answer = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]
popList = [] # 삭제할 리스트
puyoCnt = 0 # 뿌요 카운트

def bfs(nodeX, nodeY):
    global puyoCnt
    puyoCnt = 0

    color = graph[nodeX][nodeY] # 연쇄 기준 컬러
    visit = [[False] * garo for _ in range(sero)]
    visit[nodeX][nodeY] = True
    q = deque()
    q.append([nodeX, nodeY])

    while(q):
        x, y = q.popleft()
        puyoCnt += 1
        popList.append([x,y])
        for i in range(4):
            mx, my = x + dx[i], y + dy[i]
            if 0 <= mx < sero and 0 <= my < garo:
                if visit[mx][my]: continue
                if graph[mx][my] == color:
                    visit[mx][my] = True
                    q.append([mx,my])

def puyoPop():
    while(popList):
        x, y = popList.pop()
        graph[x][y] = '.'
    return False

def puyoDown(y):
    # 아래 -> 위 순서 탐색
    for x in range(10, -1, -1):
        for mx in range(x, 11):
            # 빈 칸이라면 내리기
            if graph[mx + 1][y] == '.':
                graph[mx + 1][y] = graph[mx][y]
                graph[mx][y] = '.'

while(True):
    isFinish = True
    for j in range(sero):
        for i in range(garo):
            if graph[j][i] != '.':
                bfs(j,i) # 연쇄 확인
                # 연쇄 가능하면 전부 터뜨리기
                if puyoCnt >= 4:
                    isFinish = puyoPop()
                else:
                    popList = []
    
    # 빈 칸 채우기
    for j in range(11, -1, -1):
        for i in range(garo):
            if graph[j][i] == '.':
                puyoDown(i)
    
    # 연쇄 끝나면 답 증가
    if isFinish == False:
        answer += 1
    else:
        break

print(answer)