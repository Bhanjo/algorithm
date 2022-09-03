import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = 10**10

graph = [[] for _ in range(n+1)]
dist = [INF for _ in range(n+1)]

for i in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append([end, cost])

target, destination = map(int, input().split())

def dijikstra(target):
    dist[target] = 0
    h = []
    heapq.heappush(h, [target, dist[target]])

    while(h):
        currNode, currDist =  heapq.heappop(h)
        if dist[currNode] < currDist:
            continue
        for nextNode, nextDist in graph[currNode]:
            totalDist = currDist + nextDist
            if dist[nextNode] > totalDist:
                dist[nextNode] = totalDist
                heapq.heappush(h, [nextNode, totalDist])

dijikstra(target)

print(dist[destination])
