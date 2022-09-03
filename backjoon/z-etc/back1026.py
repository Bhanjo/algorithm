import sys
input = sys.stdin.readline

size = int(input())
answer = 0
nums = []

for i in range(2):
    item = list(map(int, input().split()))
    if i == 1:
        item.sort(reverse=True)
    else:
        item.sort()
    nums.append(item)

for i in range(size):
    answer += nums[0][i] * nums[1][i]

print(answer)