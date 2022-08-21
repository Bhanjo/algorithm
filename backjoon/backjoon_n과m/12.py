import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
temp = []
answer = []

def dfs(target):
    if len(temp) == m:
        answer.append(temp[:])
        return
    saveNum = 0
    for i in range(n):
        if target <= nums[i] and saveNum != nums[i]:
            saveNum = nums[i]
            temp.append(nums[i])
            dfs(nums[i])
            temp.pop()

dfs(0)
for i in answer:
    print(*i)