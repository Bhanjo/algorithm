import sys
input = sys.stdin.readline

start = int(input())
end = int(input())
answer = 0
minVal = 10**8
nums = [True for _ in range(end+1)]

def primes(n):
    nums[0], nums[1] = False, False
    target = int(n**1/2)
    for i in range(2, target):
        if nums[i]:
            for j in range(i*2, n+1, i):
                nums[j] = False

primes(end)

for i in range(start, end+1):
    if nums[i]:
        answer += i
        minVal = min(minVal, i)
if answer > 0:
    print(answer)
    print(minVal)
else:
    print(-1)