import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

distance = [10**10 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for i in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

origin, destination = map(int, input().split())

def dijikstra(node):
    h = []
    distance[node] = 0
    heapq.heappush(h, (distance[node], node))
    while(h):
        currDist, currNode = heapq.heappop(h)
        if currDist > distance[currNode]: continue
        for nextNode, nextDist in graph[currNode]:
            totalDist = distance[currNode] + nextDist
            if totalDist < distance[nextNode]:
                distance[nextNode] = totalDist
                heapq.heappush(h, (totalDist, nextNode))

dijikstra(origin)
print(distance[destination])