def solution(S):
    cnt = 0
    for i in S:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return 0

    return 1 if cnt == 0 else 0
    pass
