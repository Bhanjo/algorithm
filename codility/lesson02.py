def solution(A, K):
    a = A
    for i in range(K):
        a.insert(0, a.pop())
    return a
    pass
