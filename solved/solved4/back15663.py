n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False] * n
temp = []

def permu():
    if len(temp) == m:
        print(*temp)
        return
    checkNum = 0
    for i in range(n):
        if not visited[i] and checkNum != nums[i]:
            visited[i] = True
            temp.append(nums[i])
            checkNum = nums[i]
            permu()
            visited[i] = False
            temp.pop()

permu()
