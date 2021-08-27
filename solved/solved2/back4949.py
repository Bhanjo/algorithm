import sys
input = sys.stdin.readline

while(True):
    string = input()
    if string == '.\n':
        break

    i = 0
    stack = []
    check = True
    while(i < len(string) - 1):
        if string[i] == '(' or string[i] == '[':
            stack.append(string[i])
        elif string[i] == ')' or string[i] == ']':
            if stack:
                pop = stack.pop()
                if (pop == '(' and string[i] == ')') or (pop == '[' and string[i] == ']'):
                    check = True
                else:
                    check = False
                    break
            else:
                check = False
                break
        i += 1
    if stack:
        check = False
    print('yes') if check else print('no')