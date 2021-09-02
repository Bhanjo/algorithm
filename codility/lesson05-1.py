def solution(A):
    cnt = 0
    result = 0
    for i in A:
        if i == 0:
            cnt += 1
        else:
            result += cnt
    if result > 1000000000:
        return -1
    return result
    pass
