import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
hashing = {}

for i in n_list:
    if i in hashing:
        hashing[i] += 1
    else:
        hashing[i] = 1

print(' '.join(str(hashing[j]) if j in hashing else '0' for j in m_list))