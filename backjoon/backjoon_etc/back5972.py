import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
dist = [10**10 for _ in range(n+1)]

for i in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
    graph[end].append((start, cost))

def dijikstra(start):
    h = []
    dist[start] = 0
    heapq.heappush(h, (start, dist[start]))
    while(h):
        currNode, currCost = heapq.heappop(h)
        if currCost > dist[currNode]: continue
        for nextNode, nextCost in graph[currNode]:
            totalCost = currCost + nextCost
            if totalCost < dist[nextNode]:
                dist[nextNode] = totalCost
                heapq.heappush(h, (nextNode, totalCost))
dijikstra(1)
print(dist[n])