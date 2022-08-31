import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
answer = 0

for n in nums:
    isPrime = True
    if n == 1:
        continue
    if n == 2 or n == 3:
        answer += 1
        continue
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            isPrime = False
            break
    if isPrime:
        answer += 1

print(answer)