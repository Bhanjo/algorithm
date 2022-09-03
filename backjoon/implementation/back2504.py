import sys
input = sys.stdin.readline

word = input().strip()
st = []
answer = 0
value = 1

for i in range(len(word)):
    if word[i] == '(':
        value *= 2
        st.append('(')
    elif word[i] == '[':
        value *= 3
        st.append('[')
    elif word[i] == ')':
        if len(st) == 0 or st[-1] == '[':
            answer = 0
            break
        if word[i-1] == '(': # 이전값이 '(' 일 때 지금까지 값 더하기
            answer += value
        st.pop()
        # x(a+b) == xa + xb이라는 분배법칙 이용
        value = value // 2
    else: # ']' 일때
        if len(st) == 0 or st[-1] == '(':
            answer = 0
            break
        if word[i-1] == '[':
            answer += value
        st.pop()
        value = value // 3

print(answer if len(st) == 0 else 0)