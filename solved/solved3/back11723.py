import sys
input = sys.stdin.readline

m = int(input())
s = set()
for i in range(m):
    cmd = input().strip().split()
    if len(cmd) == 1:
        if cmd[0] == 'all':
            s = set([i for i in range(1,21)])
        elif cmd[0] == 'empty':
            s = set()
    else:
        num = int(cmd[1])
        if cmd[0] == 'add' and num not in s:
            s.add(num)
        elif cmd[0] == 'remove' and num in s:
            s.discard(num)
        elif cmd[0] == 'check':
            print(1 if num in s else 0)
        elif cmd[0] == 'toggle':
            if num not in s:
                s.add(num)
            elif num in s:
                s.discard(num)