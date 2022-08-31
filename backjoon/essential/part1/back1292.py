import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = []
cnt = 0

for i in range(1, 1000):
    for j in range(i):
        nums.append(i)
        cnt += 1
    if cnt >= m:
        break

print(sum(nums[n-1:m]))
