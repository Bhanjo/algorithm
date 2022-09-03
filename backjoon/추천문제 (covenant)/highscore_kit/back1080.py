import sys
input = sys.stdin.readline

answer = 0
n, m = map(int, input().split())

# str 타입
graph = [list(input().strip()) for _ in range(n)]
target = [list(input().strip()) for _ in range(n)]

def flip(x,y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            graph[i][j] = '1' if graph[i][j] == '0' else '0'

for i in range(n-2):
    for j in range(m-2):
        if graph[i][j] != target[i][j]:
            flip(i,j)
            answer += 1

if graph != target:
    answer = -1

print(answer)
