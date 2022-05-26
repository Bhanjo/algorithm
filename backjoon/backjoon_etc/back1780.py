import sys
input = sys.stdin.readline

n = int(input())
graph = []
cnt = [0,0,0]
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

def divcon(x, y, n):
    target = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if target != graph[i][j]:
                # 9등분 하기
                for c in range(3):
                    for r in range(3):
                        divcon(x + c * n // 3, y + r * n // 3, n // 3)
                return
    
    if target == -1:
        cnt[0] += 1
    if target == 0:
        cnt[1] += 1
    if target == 1:
        cnt[2] += 1

divcon(0, 0, n)
for i in cnt:
    print(i)