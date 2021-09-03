def solution(S):
    stack = []
    for i in S:
        if i == '(' or i == '[' or i == '{':
            stack.append(i)
        elif stack:
            pop = stack.pop()
            if (pop == '(' and i == ')') or (pop == '[' and i == ']') or (pop == '{' and i == '}'):
                continue
            else:
                return 0
        else:
            return 0
    if stack:
        return 0
    else:
        return 1
    pass
