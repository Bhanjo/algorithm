import sys

a = int(input())
num = []
for _ in range(a):
    num.append(int(sys.stdin.readline()))

for i in sorted(num):
    sys.stdout.write(str(i) + "\n")