import sys
input = sys.stdin.readline

tc = int(input())
stack = []
for _ in range(tc):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))
