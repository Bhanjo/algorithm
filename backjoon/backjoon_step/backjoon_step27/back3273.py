import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
target = int(input())
start, end, answer = 0, n - 1, 0

while start < end:
    hap = nums[start] + nums[end]
    if hap == target:
        answer += 1
    if hap < target:
        start += 1
        continue
    end -= 1

print(answer)