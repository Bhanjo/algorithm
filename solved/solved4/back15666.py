import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
ans = []

def DFS(count, visit):
    if count == m:
        print(' '.join(map(str, ans)))
        return
    checkNum = 10001
    for i in range(n):
        if visit <= nums[i] and checkNum != nums[i]:
            ans.append(nums[i])
            checkNum = nums[i]
            DFS(count + 1, nums[i])
            ans.pop()

DFS(0, -1)