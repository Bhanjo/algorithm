import sys
input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
    garo = list(map(int, input().split()))
    graph.append(garo)

for i in range(1,n):
    graph[i][0] += graph[i-1][0]
    graph[i][i] += graph[i-1][i-1]

for i in range(2,n):
    for j in range(1,i):
        graph[i][j] = max(graph[i][j] + graph[i-1][j-1], graph[i][j] + graph[i-1][j])

print(max(graph[n-1]))