import copy
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
visit = [False for _ in range(N)]
nums = [i+1 for i in range(N)]
temp = []
answer = []

def dfs():
    if len(temp) == M:
        answer.append(copy.deepcopy(temp))
        return
    for i in range(len(visit)):
        if not visit[i]:
            temp.append(nums[i])
            dfs()
            temp.pop()

dfs()
for i in answer:
    print(*i)