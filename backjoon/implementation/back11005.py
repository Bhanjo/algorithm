import sys
input = sys.stdin.readline

n, b = map(int, input().split())
ans = ''
nums = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while(n > 0):
    num = n % b
    ans += nums[num]
    n = n // b
print(ans[::-1])