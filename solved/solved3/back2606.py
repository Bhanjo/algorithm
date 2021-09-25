import sys
input = sys.stdin.readline

c = int(input())
m = int(input())
graph = [[]*c for _ in range(c+1)]
for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

cnt = 0


def dfs(graph, start, visited=[1]):
    global cnt
    for node in graph[start]:
        if node not in visited:
            cnt += 1
            visited.append(node)
            dfs(graph, node, visited)

    return cnt


dfs(graph, 1)
print(cnt)
