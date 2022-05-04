def divBraket(p):
    isOpen = 0
    isClose = 0
    for i in range(len(p)):
        if p[i] == '(':
            isOpen += 1
        else:
            isClose += 1
        if isOpen == isClose:
            return [p[:i+1], p[i+1:]]

def isPerfect(u):
    st = []
    for i in u:
        if i == '(':
            st.append(i)
        else:
            if len(st) == 0:
                return False
            st.pop()
    return True
        
def solution(p):
    answer = ''
    # 조건 1
    if p == '':
        return ''
    # 조건 2
    u, v = divBraket(p)
    # 조건 3
    if isPerfect(u):
        return u + solution(v)
    else:
        answer = '(' # 조건 4-1
        answer += solution(v) # 조건 4-2
        answer += ')' # 조건 4-3
        # 조건 4-4
        for i in u[1:-1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('
    return answer