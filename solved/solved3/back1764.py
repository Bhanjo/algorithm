import sys
input = sys.stdin.readline
dict = {}
n, m = map(int, input().split())
cnt = 0
ans = []
for i in range(n):
    name = input().strip()
    dict[name] = name
for i in range(m):
    findName = input().strip()
    a = dict.get(findName, 0)
    if a != 0:
        ans.append(a)
        cnt += 1
print(cnt)
ans.sort()
for i in ans:
    print(i)