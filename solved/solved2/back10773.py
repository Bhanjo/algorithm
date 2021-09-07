import sys
input = sys.stdin.readline

tc = int(input())
stack = []
hap = 0
for _ in range(tc):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))
