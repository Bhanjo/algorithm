import sys
from collections import deque
input = sys.stdin.readline

node, edge = map(int, input().split())
graph = [[] for _ in range(node + 1)]
q = deque()

for i in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, startNode):
    # startNode의 모든 케빈 구하기
    kebin = [0] * (node + 1)
    q = deque()
    visit[startNode] = 1
    q.append(startNode)
    while(q):
        currNode = q.popleft()
        for i in graph[currNode]:
            if visit[i] == 0:
                visit[i] = 1
                # 비용 구하기
                kebin[i] = kebin[currNode] + 1
                q.append(i)

    return sum(kebin)

allKebin = []
for i in range(1, node + 1):
    visit = [0 for _ in range(node + 1)]
    allKebin.append(bfs(graph, i))

print(allKebin.index(min(allKebin)) + 1)