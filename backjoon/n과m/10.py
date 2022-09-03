import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
temp = []
visit = [False for _ in range(n)]

# 방법1
dir = {}
def dfs(target):
    if len(temp) == m:
        t = ' '.join(map(str, temp))
        if t not in dir:
            print(*temp)
            dir[t] = True
        return
    for i in range(len(nums)):
        if not visit[i] and target <= nums[i]:
            visit[i] = True
            temp.append(nums[i])
            dfs(nums[i])
            temp.pop()
            visit[i] = False
dfs(0)

# 방법2
def dfs(target):
    if len(temp) == m:
        print(*temp)
        return
    saveNum = 0
    for i in range(target, n):
        if not visit[i] and saveNum != nums[i]:
            visit[i] = True
            temp.append(nums[i])
            saveNum = nums[i]
            dfs(i+1)
            temp.pop()
            visit[i] = False

dfs(0)