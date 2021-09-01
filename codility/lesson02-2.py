def solution(A):

    A = sorted(A)

    while A:
        try:
            a = A.pop()
            b = A.pop()
        except:
            break

        if not a == b:
            break

    return a
