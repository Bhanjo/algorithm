import sys
input = sys.stdin.readline

N = map(int, input().split())

A =set(map(int, input().split()))
B = set(map(int, input().split()))

ress = A-B

res = sorted(ress)
print(len(res))

if len(res) !=0:
    print(*(res))