import sys

a = int(sys.stdin.readline())
num = []
for _ in range(a):
    num.append(list(map(int, sys.stdin.readline().split())))

num.sort(key=lambda num:(num[1],num[0]))
for i in range(len(num)):
    sys.stdout.write(str(num[i][0]) + " " + str(num[i][1]) + "\n")