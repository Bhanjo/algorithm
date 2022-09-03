import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visit = [False for _ in range(n)]

temp = []
answer = []

def dfs(val):
    if len(temp) == m:
        answer.append(temp[:])
        return
    for i in nums:
        if i > val:
            temp.append(i)
            dfs(i)
            temp.pop()

dfs(0)
for i in answer:
    print(*i)