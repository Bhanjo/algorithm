import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
graph = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]
ans = []
dictAns = dict()
for i in range(n+1):
    dictAns[i] = []

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    if visit[node] == 0:
        visit[node] = 1
        for i in graph[node]:
            keys, val = min(node, i),  max(node, i)
            if val not in dictAns[keys]:
                dictAns[keys].append(val)
                ans.append([node, i])
            dfs(i)
dfs(1)
ans.sort(key=lambda item:item[1])
for i in ans:
    print(i[0])