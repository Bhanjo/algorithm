import sys
input = sys.stdin.readline

n,m = map(int,input().split())
nums = list(map(int, input().split()))
nums.sort()
visit = [False for _ in range(n)]

answer = []
temp = []

def dfs(depth):
    if depth == m:
        t = temp[:]
        answer.append(t)
        return
    for i in range(len(visit)):
        if not visit[i]:
            visit[i] = True
            temp.append(nums[i])
            dfs(depth+1)
            temp.pop()
            visit[i] = False
dfs(0)
for i in answer:
    print(*i)