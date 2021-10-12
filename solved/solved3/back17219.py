import sys
input = sys.stdin.readline

n, m = map(int, input().split())
password_list = dict()
for _ in range(n):
    addr, pw = map(str, input().split())
    password_list[addr] = pw

for i in range(m):
    print(password_list[str(input().strip())])
