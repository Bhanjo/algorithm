import sys
input = sys.stdin.readline

n = int(input())
graph = []
answer = ''

for i in range(n):
    row = list(input().strip())
    graph.append(row)

def divcon(x, y, n):
    global answer
    target = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if target != graph[i][j]:
                answer += '('
                for c in range(2):
                    for r in range(2):
                        divcon(x + c * n // 2, y + r * n // 2, n // 2)
                answer += ')'
                return

    if target == '0':
        answer += '0'
    else:
        answer += '1'

divcon(0,0,n)
print(answer)