# 62.5/100
import heapq

def solution(n, roads, sources, destination):
    answer = []
    graph = [[]*(n+1) for _ in range(n+1)]

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


# 
import heapq
from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    graph = [[]*(n+1) for _ in range(n+1)]

    for i in roads:
        start, end = i[0], i[1]
        graph[start].append(end)
        graph[end].append(start)

    q = deque()
    q.append(destination)
    visit = [[False]*(n+1) for _ in range(n+1)]
    dist = [100000]*(n+1)
    dist[destination] = 0

    while(q):
        currNode = q.popleft()
        for i in graph[currNode]:
            if not visit[currNode][i]:
                visit[currNode][i] = True
                dist[i] = min(dist[i], dist[currNode] + 1)
                q.append(i)
    
    for i in range(len(dist)):
        if i in sources:
            if dist[i] < 100000:
                answer.append(dist[i])
            else:
                answer.append(-1)
    return answer