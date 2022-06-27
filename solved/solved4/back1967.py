import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for i in range(n-1):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
    graph[end].append((start, cost))

def dfs(node, cost):
    for nextNode, nextCost in graph[node]:
        if dist[nextNode] == -1: # 아직 방문하지 않았다면
            # 기준점에서 해당 노드까지의 길이 =
            # 지금까지 온 길이(cost) + node에서 nextNode까지의 비용(nextCost)
            dist[nextNode] = cost + nextCost
            dfs(nextNode, dist[nextNode])

# root에서 각 노드까지 길이 구하기 (가장 먼 곳 찾기)
dist = [-1]*(n+1)
dist[1] = 0
dfs(1, 0)

# 가장 먼 곳을 기준으로 가장 먼 곳 찾기
mostLongDistance = dist.index(max(dist))
dist = [-1]*(n+1) # 방문확인 및 비용 초기화
dist[mostLongDistance] = 0
dfs(mostLongDistance, 0)

print(max(dist))