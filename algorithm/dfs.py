# dfs 알고리즘 기초

graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']


def stack_dfs(graph, start_node):  # stack을 이용한 방법
    not_visited, visited = list(), list()
    not_visited.append(start_node)

    while not_visited:
        node = not_visited.pop()
        if node not in visited:
            print(node)
            visited.append(node)
            not_visited.extend(graph[node])

    return visited


# stack_dfs(graph, 'A')

def recursive_dfs(graph, start, visited=[]):  # 재귀 dfs
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            recursive_dfs(graph, node, visited)
            print(node)
    return visited


recursive_dfs(graph, 'A')

# DFS 빈출 유형 (1967번)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n+1)]


def dfs(x, wei):
    for i in graph[x]:
        a, b = i
        if distance[a] == -1:
            distance[a] = wei + b
            dfs(a, wei + b)


# 트리 구현
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

# 1번 노드에서 가장 먼 곳을 찾는다.
distance = [-1] * (n + 1)
distance[1] = 0
dfs(1, 0)

# 위에서 찾은 노드에 대한 가장 먼 노드를 찾는다.
start = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[start] = 0
dfs(start, 0)

print(max(distance))