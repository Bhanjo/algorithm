import sys
from unittest import result
input = sys.stdin.readline

n = int(input())
graph = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

# 플로이드 와샬 알고리즘
for layover in range(n):
    for start in range(n):
        for end in range(n):
            if graph[start][layover] == 1 and graph[layover][end] == 1:
                graph[start][end] = 1

for i in graph:
    row = ''
    for j in i:
        row += str(j)
        row += ' '
    print(row)