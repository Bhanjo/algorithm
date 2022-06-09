import sys
input = sys.stdin.readline

n,m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visit = [0 for _ in range(n)]
ans = []

def permu(count, n, m):
    if count == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(n):
        if count == 0 or ans[count - 1] <= nums[i]: # 방문한 노드 <= 지금 노드 인것만 추가
            ans.append(nums[i])
            permu(count + 1, n, m)
            ans.pop()

permu(0, n, m)