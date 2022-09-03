import sys
input = sys.stdin.readline

braket = list(map(str, input().strip()))
stack = []
temp = 1 # 곱하는 값
answer = 0 # 더하는 값

for idx, i in enumerate(braket):
    # 여는 괄호일 때 temp에 값 곱하기
    if i == '(':
        stack.append('(')
        temp = temp * 2
    if i == '[':
        stack.append('[')
        temp = temp * 3
    # 닫는 괄호, 이전괄호가 여는 괄호일 때 => answer에 더하고 temp 값을 이전 상태로 만들기
    if i == ']':
        if len(stack) == 0:
            answer = 0
            break
        b = stack.pop()
        if not b == '[':
            answer = 0
            break
        # 중복 덧셈을 막기 위해 이전 값이 여는 괄호일 때만 더하기
        if braket[idx-1] == '[':
            answer += temp
        temp = temp // 3
    if i == ')':
        if len(stack) == 0:
            answer = 0
            break
        b = stack.pop()
        if not b == '(':
            answer = 0
            break
        if braket[idx-1] == '(':
            answer += temp
        temp = temp // 2
if len(stack) != 0:
    answer = 0

print(answer)

# 2회차
n = list(input().strip())
st = []
temp = 1
answer = 0

for i, braket in enumerate(n):
    if braket == '(' or braket =='[':
        st.append('(' if braket == '(' else '[')
        temp = temp * 2 if braket == '(' else temp * 3
    
    if braket == ')' or braket == ']':
        if len(st) == 0:
            answer = 0
            break
        b = st.pop()
        if (b == '(' and braket == ')') or (b == '[' and braket == ']'):
            if n[i-1] == '(' or n[i-1] == '[':
                answer += temp
            temp = temp // 2 if b == '(' else temp // 3
        else:
            answer = 0
            break

print(answer if len(st) == 0 else 0)