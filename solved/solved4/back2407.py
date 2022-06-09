import sys
input = sys.stdin.readline
n, m = map(int, input().split())

facto = [1,1]
for i in range(2, n + 1):
    facto.append(facto[i-1] * i)
print(facto[n] // (facto[n-m] * facto[m]))