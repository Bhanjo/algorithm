import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
temp = []

def dfs():
    if len(temp) == m:
        print(*temp)
        return
    saveNum = 0
    for i in range(n):
        if saveNum != nums[i]:
            temp.append(nums[i])
            saveNum = nums[i]
            dfs()
            temp.pop()

dfs()