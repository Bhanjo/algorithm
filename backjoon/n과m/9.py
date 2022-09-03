import sys
input = sys.stdin.readline

n,m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visit = [False for _ in range(n)]
temp = []
answer = []
dir = {}

def dfs():
    if len(temp) == m:
        t = ' '.join(map(str, temp))
        if t not in dir:
            answer.append(temp[:])
            dir[t] = True
        return
    for i in range(len(nums)):
        if not visit[i]:
            visit[i] = True
            temp.append(nums[i])
            dfs()
            temp.pop()
            visit[i] = False
dfs()
for i in answer:
    print(*i)