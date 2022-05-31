import sys
input = sys.stdin.readline

n = int(input())
nemo = [0]*1001
nemo[0], nemo[1], nemo[2] = 0, 1, 3
for i in range(3, n + 1):
    nemo[i] = nemo[i-1] + (nemo[i-2] * 2)
print(nemo[n] % 10007)