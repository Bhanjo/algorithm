# 62.5/100
import heapq

def solution(n, roads, sources, destination):
    answer = []
    # graph = [[]*(n+1) for _ in range(n+1)]
    graph = {i+1: [] for i in range(n)}

    for i in roads:
        start, end = i[0], i[1]
        graph[start].append((end,1))
        graph[end].append((start,1))

    # 출발->도착
    for start in sources:
        distance = [100000000 for _ in range(n+1)]
        distance[start] = 0
        h = []
        heapq.heappush(h, (distance[start], start))
        
        while(h):
            currDist, currNode = heapq.heappop(h)
            if distance[currNode] < currDist:
                continue
            for nextNode, nextDist in graph[currNode]:
                totalDist = currDist + nextDist
                if totalDist < distance[nextNode]:
                    distance[nextNode] = totalDist
                    heapq.heappush(h, (totalDist, nextNode))
    
        # print(distance)
        answer.append(distance[destination] if distance[destination] < 100000000 else -1)

    return answer


# 2회차
from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n+1)]

    for i in roads:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    
    visit = [-1] * (n+1)

    def bfs():
        q = deque()
        q.append(destination)
        visit[destination] = 0
        while(q):
            currNode = q.popleft()
            for i in graph[currNode]:
                if visit[i] == -1:
                    visit[i] = visit[currNode] + 1
                    q.append(i)

    bfs()
    for i in sources:
        answer.append(visit[i])
        
    return answer