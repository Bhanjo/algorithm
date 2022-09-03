import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
temp = []
answer = []

def dfs(num):
    if len(temp) == m:
        answer.append(temp[:])
        return
    for i in nums:
        if i >= num:
            temp.append(i)
            dfs(i)
            temp.pop()

dfs(0)
for i in answer:
    print(*i)