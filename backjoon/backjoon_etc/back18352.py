import heapq
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
nodes = [[] for _ in range(n + 1)]

INF = 1000000000
cost = [INF] * (n + 1) # 최소값을 위해 모든 거리 초기화

for i in range(m):
    start, to = map(int, input().split())
    nodes[start].append((to, 1)) # 노드에 단방향 연결 만들기

def dijkstra(start):
    h = []
    heapq.heappush(h, (0, start)) # 시작지점 세팅
    cost[start] = 0
    while(h):
        dist, now = heapq.heappop(h)
        if cost[now] < dist: continue # 현재 노드의 최소 거리 < 해당 노드 거리
        for i in nodes[now]:
            # 다음 노드 거리 = 현재 노드 값 + 현재 노드에서 다음 노드까지 가는 거리
            nextDist = dist + i[1]
            if nextDist < cost[i[0]]:
                cost[i[0]] = nextDist
                # 다음 노드 탐색
                heapq.heappush(h, (nextDist, i[0]))

dijkstra(x)
answer = []
for i in range(1, n + 1):
    if cost[i] == k:
        answer.append(i)

if len(answer) == 0:
    print(-1)
else:
    for i in answer:
        print(i)