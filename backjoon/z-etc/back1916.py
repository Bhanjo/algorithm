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

# 2회차
import heapq
n = int(input())
edge = int(input())
graph = [[] for _ in range(n+1)]
costs = [100000000 for _ in range(n+1)]

for i in range(edge):
    start, end, cost = map(int, input().split())
    graph[start].append([end, cost])

startPoint, endPoint = map(int, input().split())

def dijikstra(startPoint):
    costs[startPoint] = 0
    h = []
    heapq.heappush(h, [startPoint, 0])

    while(h):
        currNode, price = heapq.heappop(h)
        if costs[currNode] < price:
            continue
        for nextNode, nextPrice in graph[currNode]:
            totalPrice = costs[currNode] + nextPrice
            if costs[nextNode] > totalPrice:
                costs[nextNode] = totalPrice
                heapq.heappush(h, [nextNode, totalPrice])

dijikstra(startPoint)
print(costs[endPoint])