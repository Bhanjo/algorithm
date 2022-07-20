import sys
input = sys.stdin.readline

answer = 0
n, m = map(int, input().split())
x, y, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

visit = [[0] * m for _ in range(n)]

# 왼쪽 탐색, 후진 (북 동 남 서)
direcion = [(0,-1), (-1,0), (0,1), (1,0)]
goback = [(1,0), (0,-1), (-1,0), (0,1)]

isOver = False
while(not isOver):
    # 1번: 현 위치 청소
    if not visit[x][y]:
        answer += 1
        visit[x][y] = 1

    # 2번: 탐색 후 동작
    i = 0
    while(True):
        # d방향 기준으로 왼쪽 탐색
        findX = x + direcion[d][0]
        findY = y + direcion[d][1]
        # 2-1번: 벽x, 청소x 
        if graph[findX][findY] == 0 and not visit[findX][findY]:
            # 방향 회전하고 전진
            d = d - 1 if d - 1 >= 0 else 3
            x = findX
            y = findY
            break # 1번으로 돌아가기
        # 2-2, 2-3번: 벽o OR 청소o / 모든 방향 탐색
        if graph[findX][findY] == 1 or visit[findX][findY]:
            # 방향 회전하고 2번으로 돌아가기
            d = d - 1 if d - 1 >= 0 else 3
            if i == 3: # 모든 방향 탐색 완료
                # 뒤로 가기
                x = x + goback[d][0]
                y = y + goback[d][1]
                if graph[x][y] == 1: # 2-4번: 후진 시 벽이라면
                    isOver = True
                    break
                else:
                    i = -1
            i += 1
print(answer)