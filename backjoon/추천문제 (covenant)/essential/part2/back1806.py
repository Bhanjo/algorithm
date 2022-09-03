import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))
left, right = 0, 0
answer = 10**10
temp = nums[0]
isExist = False

while(left < len(nums)):
    # 목표 값 구했다면 최소값 갱신
    if temp >= s:
        isExist = True
        answer = min(answer, right-left+1)
        temp -= nums[left]
        left += 1
    else:
        right += 1
        if right >= len(nums):
            break
        temp += nums[right]

print(answer if isExist else 0)
