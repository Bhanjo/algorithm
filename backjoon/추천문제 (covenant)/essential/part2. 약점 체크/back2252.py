from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
indegree = [0 for _ in range(n+1)] # 진입 차수 count
graph = [[] for _ in range(n+1)]
answer = []

for i in range(m):
    start, end = map(int,input().split())
    graph[start].append(end)
    indegree[end] += 1

def topologySort():
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    while(q):
        node = q.popleft()
        answer.append(node)
        for i in graph[node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

topologySort()
print(*answer)

# 복습
from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[] for _ in range(n)]
edges = [0 for _ in range(n)]
answer= []

for i in range(m):
    start, end = map(int, input().split())
    graph[start-1].append(end-1)
    edges[end-1] += 1

def topolSort():
    q = deque()
    for idx, edge in enumerate(edges):
        if edge == 0:
            q.append(idx)
    while(q):
        node = q.popleft()
        answer.append(node+1)
        for i in graph[node]:
            edges[i] -= 1
            if edges[i] == 0:
                q.append(i)

topolSort()
print(*answer)