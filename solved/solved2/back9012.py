import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    vps = str(input())
    stack = []
    check = False
    for i in range(len(vps)-1):
        if vps[i] == '(':
            stack.append('(')
        else:
            if stack:
                right = stack.pop()
                if right == '(' and vps[i] == ')':
                    check = True
                else:
                    check = False
                    break
            else:
                check = False
                break
    if stack:
        check = False
    print('YES') if check else print('NO')