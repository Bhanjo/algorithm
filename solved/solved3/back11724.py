import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
graph = [[]*i for i in range(n+1)]
checked = []

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(a):
    checked.append(a)
    for i in graph[a]:
        if i not in checked:
            dfs(i)


cnt = 0
for w in range(1, n+1):
    if w not in checked:
        dfs(w)
        cnt += 1
print(cnt)
