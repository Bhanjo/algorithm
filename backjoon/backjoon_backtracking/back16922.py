import sys
input = sys.stdin.readline

graph = [1, 5, 10, 50]
answer = 0
n = int(input())
visit = [False]*10001

def dfs(cnt, idx, choose):
    global answer
    if cnt == n:
        if visit[choose] == False:
            visit[choose] = True
            answer += 1
        return
    for i in range(idx, len(graph)):
        dfs(cnt + 1, i, choose + graph[i])
dfs(0, 0, 0)
print(answer)