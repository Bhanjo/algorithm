# https://blog.naver.com/PostView.naver?blogId=ndb796&logNo=221282478466
# - LCA 동작 과정
#     - 모든 노드에 대한 깊이 구하기
#     - 모든 노드에 대해 2**i번째 부모 노드 구하기
#     - LCA를 찾을 두 노드 설정
#     - 두 노드 깊이가 동일하도록 거슬러 올라가기
#     - 최상단 노드부터 내려오며 두 노드의 공통 부모 찾기

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
parent = [0 for _ in range(n+1)]
depth = [0 for _ in range(n+1)]
visit = [False for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for i in range(n-1):
    x, y = map(int, input().split())
    # 양방향 노드
    graph[x].append(y)
    graph[y].append(x)

# 깊이 탐색을 이용해 root 노드 부터 차례대로 레벨(depth) 구하기
def dfs(node, level):
    visit[node] = True
    depth[node] = level

    # 방문하지 않은 노드(nextNode)의 부모를 node로 설정
    for nextNode in graph[node]:
        if not visit[nextNode]:
            parent[nextNode] = node
            dfs(nextNode, level + 1)

# 최소 공통 조상 핵심
def lca(node1, node2):
    # 두 노드의 깊이가 맞춰질 때까지 부모로 거슬러 올라가기
    while depth[node1] != depth[node2]:
        if depth[node1] > depth[node2]:
            node1 = parent[node1]
        else:
            node2 = parent[node2]
    
    # 그 후 동시에 부모로 올라가며 서로 같을 때(부모 찾을 때) 찾기
    while node1 != node2:
        node1 = parent[node1]
        node2 = parent[node2]
    
    return node1 # 공통 조상, node2도 가능

dfs(1,0)
for _ in range(int(input())):
    x, y = map(int, input().split())
    print(lca(x,y))