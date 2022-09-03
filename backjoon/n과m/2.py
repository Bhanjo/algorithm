import sys
import copy
input = sys.stdin.readline

N, M = map(int, input().split())
visit = [False for _ in range(N)]
answer = []

def dfs(arr, depth):
    global visit
    if depth == M:
        answer.append(copy.deepcopy(arr))
        return
    for i in range(len(visit)):
        if not visit[i]:
            if not arr or i+1 > arr[-1]:
                visit[i] = True
                arr.append(i+1)
                dfs(arr, depth+1)
                arr.pop()
                visit[i] = False


dfs([], 0)
for i in answer:
    print(*i)