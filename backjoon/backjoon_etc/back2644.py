# DFS
import sys
input = sys.stdin.readline


def dfs(node):
    for i in graph[node]:
        if visited[i] == 0:
            visited[i] = visited[node] + 1
            dfs(i)


n = int(input())
graph = [[] for i in range(n+1)]
p1, p2 = map(int, input().split())

for _ in range(int(input())):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (n+1)
dfs(p1)
print(visited[p2] if visited[p2] > 0 else -1)
