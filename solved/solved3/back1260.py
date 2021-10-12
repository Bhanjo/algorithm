import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[]*(n+1) for _ in range(n+1)]
visit_1 = []
visit_2 = []
queue = deque()
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()


def DFS(node):
    if node not in visit_1:
        visit_1.append(node)
        for i in graph[node]:
            DFS(i)
    return visit_1


def BFS(node):
    queue.append(node)
    while(queue):
        new = queue.popleft()
        if new not in visit_2:
            visit_2.append(new)
            for i in graph[new]:
                queue.append(i)
    return visit_2


print(*DFS(v))
print(*BFS(v))
