from collections import deque

def solution(maps):
    q = deque()
    x, y = len(maps), len(maps[0])
    visit = [[0] * y for _ in range(x)]
    cost = [[1000000] * y for _ in range(x)]
    cost[0][0] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q.append([0,0])
    
    while(q):
        currX, currY = q.popleft()
        if visit[currX][currY] == 0:
            visit[currX][currY] = 1
            for i in range(4):
                nextX, nextY = currX+dx[i], currY+dy[i]
                if (0 <= nextX < x) and (0 <= nextY < y):
                    if maps[nextX][nextY] == 1:
                        cost[nextX][nextY] = min(cost[nextX][nextY], cost[currX][currY] + 1)
                        q.append([nextX, nextY])
    
    answer = cost[x - 1][y - 1] + 1 if visit[x - 1][y - 1] == 1 else -1
    return answer

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])