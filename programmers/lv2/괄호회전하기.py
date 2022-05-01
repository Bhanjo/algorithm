def solution(s):
    brakets = ["(", "[", "{"]
    answer = 0
    for i in range(len(s)):
        st = []
        isCorrect = False
        for i in s:
            if i in brakets:
                st.append(i)
            else:
                if len(st) == 0:
                    isCorrect = False
                    break
                else:
                    com = st.pop(-1)
                    if((com == "{" and i == "}") or (com == "(" and i == ")") or (com == "[" and i == "]")):
                        isCorrect = True
                    else:
                        isCorrect = False
                        break

        if isCorrect and len(st) == 0:
            answer += 1
        s = s[1:] + s[0]
    return answer

# 다른 풀이
def solution(s):
    count = 0
    i = 0
    for i in range(len(s)):
        stack = []
        for j in s:
            if not stack:
                stack.append(j)
                continue
            if stack[-1] == '[' and j == ']':
                stack.pop()
            elif stack[-1] == '{' and j == '}':
                stack.pop()
            elif stack[-1] == '(' and j == ')':
                stack.pop()
            else:
                stack.append(j)
        s = s[1:] + s[0]
        if not stack:
            count += 1
    return count