def solution(A):
    A.sort()
    result = 0
    if 1 not in A:
        result = 1
    elif len(A)+1 not in A:
        result = len(A)+1
    else:
        for i in range(len(A)-1):
            if A[i+1] - A[i] > 1:
                result = i + 2
    return result
    pass
