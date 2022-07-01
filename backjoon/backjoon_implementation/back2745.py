import sys
input = sys.stdin.readline

nums = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n, b = map(str, input().split())
b = int(b)
n = n[::-1]
hap = 0
for i in range(len(n)):
    hap += nums.index(n[i])*(b**i)
print(hap)
