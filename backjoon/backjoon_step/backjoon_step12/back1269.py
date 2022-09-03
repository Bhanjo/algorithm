import sys
input = sys.stdin.readline

n, m = map(int,input().split())
a = set(list(map(int,input().split())))
b = set(list(map(int,input().split())))
cnt = n + m
cross = a & b # 합집합

print(cnt - len(list(cross)) * 2)