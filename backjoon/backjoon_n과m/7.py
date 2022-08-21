import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

temp = []
answer = []

def dfs():
    if len(temp) == m:
        answer.append(temp[:])
        return
    for i in nums:
        temp.append(i)
        dfs()
        temp.pop()

dfs()
for i in answer:
    print(*i)