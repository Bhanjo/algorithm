from itertools import permutations

def ops(n1, n2, o):
    if o == '*':
        return str(int(n1) * int(n2))
    elif o == '+':
        return str(int(n1) + int(n2))
    elif o == '-':
        return str(int(n1) - int(n2))

def calc(expression, op):
    arr = []
    num = ''
    for i in expression:
        if i.isdigit() == True:
            num += i
        else:
            arr.append(num)
            arr.append(i)
            num = ''
    arr.append(num)

    for o in op:
        st = []
        while len(arr) > 0:
            temp = arr.pop(0)
            if temp == o:
                # 스택 맨 뒤, 수식 맨 앞 = 숫자 두 개
                st.append(ops(st.pop(), arr.pop(0), o))
            else:
                st.append(temp)
        arr = st
    
    return abs(int(arr[0]))

def solution(expression):
    answer = []
    op = list(permutations(['*', '+', '-'], 3))
    for i in op:
        answer.append(calc(expression, i))
    return max(answer)

solution("100-200*300-500+20")
solution("50*6-3*2")
solution("100-200+300*500*20")