from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
nums = [i+1 for i in range(n)]
nums = deque(nums)

answer = []
while(len(nums) >= 2):
    answer.append(nums.popleft())
    nums.append(nums.popleft())

print(*answer, nums[0])