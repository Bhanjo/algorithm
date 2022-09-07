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