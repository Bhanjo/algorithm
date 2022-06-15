import heapq
import sys
input = sys.stdin.readline

n, e = map(int,input().split())
graph = [[]*(n+1) for _ in range(n+1)] # 2차원 배열로 그래프 표현
start = int(input())
distance = [10000000000 for _ in range(n+1)]

for i in range(e):
    u,v,w = map(int, input().split())
    graph[u].append((v,w)) # 값 넣기, w는 10 이하 정수, 메모리를 위해 값이 들어갈때만 추가하기

def dijikstra(graph, start):
    distance[start] = 0 # 시작점의 비용 = 0

    h = []
    heapq.heappush(h, (distance[start], start)) # 최소힙에 (노드비용, 노드) 넣기

    while(h):
        currDist, currNode = heapq.heappop(h) # 힙에서 노드 꺼내기
        if distance[currNode] < currDist: # 현재 노드 최소비용 < 현재 노드의 비용 이라면 건너뜀
            continue
        for nextNode, nextDist in graph[currNode]:
            totalDist = currDist + nextDist # 현재 노드 경유해서 다음 노드까지 가는데 걸리는 비용
            if totalDist < distance[nextNode]: # 위에 값이 해당 노드까지 가는 최소비용인가
                distance[nextNode] = totalDist
                # 최소 비용이므로 최소 비용 노드에서 다시 최소 비용 탐색
                heapq.heappush(h, (totalDist, nextNode))
    
    for i in distance[1:]:
        print(i) if i < 10000000000 else print('INF')

dijikstra(graph, start)