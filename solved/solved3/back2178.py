import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
miro = []


for i in range(n):
    miro.append(list(map(int,input().strip())))

def bfs(x,y):
    pos = [[-1,0],[1,0],[0,-1],[0,1]]
    q = deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()
        for i in pos:
            posX = x + i[0]
            posY = y + i[1]
            
            if(posX < 0 or posX >= n or posY < 0 or posY >= m) or miro[posX][posY] == 0:
                continue
            
            if miro[posX][posY] == 1:
                # 현 위치 비용 = 이전 위치 비용 + 1
                miro[posX][posY] = miro[x][y] + 1
                q.append((posX,posY))

    print(miro[n-1][m-1])

bfs(0,0)