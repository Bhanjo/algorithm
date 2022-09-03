import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = [i+1 for i in range(N)]
visit = [False for _ in range(N)]
answer = []

def dfs(nums, arr, depth):
    global visit
    if depth == M:
        print(*arr)
        return
    for i in range(len(nums)):
        if not visit[i]:
            visit[i] = True
            arr.append(nums[i])
            dfs(nums,arr,depth+1)
            arr.pop()
            visit[i] = False

dfs(nums, [], 0)