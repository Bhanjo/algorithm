import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
minVal = 10**10
maxVal = -10**10

for i in nums:
    if minVal > i:
        minVal = i
    if maxVal < i:
        maxVal = i
        
print(minVal, maxVal)