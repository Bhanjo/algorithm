from collections import deque

def bfs(table):
    q = deque()
    q.append([0,0])
    visit = [[0]*5 for _ in range(5)]
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    while(q):
        currX, currY = q.popleft()
        if not visit[currX][currY]:
            visit[currX][currY] = 1
            if table[currX][currY] == "O":
                if currX - 1 >= 0 and currX - 1 < 5 and currX + 1 >= 0 and currX + 1 < 5:
                    check1, check2 = table[currX - 1][currY], table[currX+1][currY]
                    if check1 == "P" and check2 == "P":
                        return 0
                if currY - 1 >= 0 and currY - 1 < 5 and currY + 1 >= 0 and currY + 1 < 5:
                    check3, check4 = table[currX][currY - 1], table[currX][currY + 1]
                    if check3 == "P" and check4 == "P":
                        return 0
            for i in range(8):
                mx, my = currX + dx[i], currY + dy[i]
                if mx >= 0 and mx < 5 and my >= 0 and my < 5:
                    if table[mx][my] == "P" and table[currX][currY] == "P":
                        if i  in [0,2,4,6]:
                            return 0
                        else:
                            checkX, checkY = currX + dx[i-1], currY + dy[i-1]
                            checkX2, checkY2 = currX + dx[i+1 if i < 7 else 0], currY + dy[i+1 if i < 7 else 0]
                            if checkX >= 0 and checkX < 5 and checkY >= 0 and checkY < 5:
                                if table[checkX][checkY] == "O":
                                    return 0
                            if checkX2 >= 0 and checkX2 < 5 and checkY2 >= 0 and checkY2 < 5:
                                if table[checkX2][checkY2] == "O":
                                    return 0
                    q.append([mx, my])
    return 1

def solution(places):
    answer = []
    for table in places:
        answer.append(bfs(table))
    return answer

solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])

# 다른 풀이
from collections import deque

def bfs(p):
    start = []
    
    for i in range(5): # 시작점이 되는 P 좌표 구하기
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i, j])
    
    for s in start:
        queue = deque([s])  # 큐에 초기값
        visited = [[0]*5 for i in range(5)]   # 방문 처리 리스트
        distance = [[0]*5 for i in range(5)]  # 경로 길이 리스트
        visited[s[0]][s[1]] = 1
        
        while queue:
            y, x = queue.popleft()
        
            dx = [-1, 1, 0, 0]  # 좌우
            dy = [0, 0, -1, 1]  # 상하

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nx<5 and 0<=ny<5 and visited[ny][nx] == 0:
                    
                    if p[ny][nx] == 'O':
                        queue.append([ny, nx])
                        visited[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1
                    
                    if p[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1


def solution(places):
    answer = []
    
    for i in places:
        answer.append(bfs(i))
    
    return answer

# 2회차
from collections import deque
# P = 사람, O = 빈공간, X = 칸막이
def ad(q, graph):
    visit = [[0]*5 for _ in range(5)]
    dist = [[0]*5 for _ in range(5)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while(q):
        x, y = q.popleft()
        visit[x][y] = 1
        for i in range(4):
            mx = dx[i] + x
            my = dy[i] + y
            if 0 <= mx < 5 and 0 <= my < 5:
                if visit[mx][my] < 1:
                    if graph[mx][my] == 'P' or graph[mx][my] == 'O':
                        dist[mx][my] += dist[x][y] + 1
                        visit[mx][my] = 1
                        if graph[mx][my] == 'P' and dist[mx][my] <= 2: # 맨허튼 거리 미준수
                            return 0
                        q.append([mx,my])
    return 1

def bfs(graph):
    ans = 1
    q = deque()
    for i in range(5):
        for j in range(5):
            if graph[i][j] == 'P':
                q.append([i,j])
                ans = ad(q, graph)
                if ans == 0:
                    return 0
    return ans

def solution(places):
    answer = []
    for i in places:
        graph = [list(j) for j in i]
        isCorrect = bfs(graph)
        answer.append(isCorrect)
    return answer