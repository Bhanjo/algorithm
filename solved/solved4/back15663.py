import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visit = [0 for _ in range(n)]
ans = []

def DFS(count): 
    if count == m:
        print(' '.join(map(str, ans)))
        return
    checkNum = 10001
    for i in range(n):
        if visit[i] == 0 and checkNum != nums[i]:
            visit[i] = 1
            checkNum = nums[i]
            ans.append(nums[i])
            DFS(count + 1)
            visit[i] = 0
            ans.pop()
DFS(0)