import sys
input = sys.stdin.readline

fibo = [0,1]
n = int(input())
for i in range(2, n+1):
    fibo.append(fibo[i-2] + fibo[i-1])
print(fibo[n])