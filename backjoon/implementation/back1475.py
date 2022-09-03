import sys
input = sys.stdin.readline

n = input().strip()
nums = [1,1,1,1,1,1,1,1,1,1]
answer = 1

for i in n:
    if nums[int(i)] > 0:
        nums[int(i)] -= 1
    elif (i == '6' or i == '9') and (nums[6] > 0 or nums[9] > 0):
        if nums[6] > 0:
            nums[6] -= 1
        elif nums[9] > 0:
            nums[9] -= 1
    else:
        answer += 1
        for k in range(10):
            nums[k] += 1
        nums[int(i)] -= 1
print(answer)