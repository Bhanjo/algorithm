import sys
input = sys.stdin.readline

n,m = map(int, input().split())
wall = list(map(int, input().split()))
graph = [[0]*m for _ in range(n)]
answer = 0

# 벽 만들기
for i, height in enumerate(wall):
    for h in range(height):
        graph[n-h-1][i] = 1

for x in range(n):
    # 좌, 우 벽 찾기
    left, right = 0, m-1
    isLeft, isRight = False, False
    while(left < right):
        if graph[x][left] == 1:
            isLeft = True
        else:
            left += 1
        if graph[x][right] == 1:
            isRight = True
        else:
            right -= 1
        if isLeft and isRight:
            break
    
    # 벽이 있다면 그 안에 물이 들어갈 수 있는 공간 찾기
    if isLeft and isRight:
        for y in range(left, right+1):
            if graph[x][y] == 0:
                answer += 1

print(answer)