# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 100%
def solution(X, A):
    leaf = [False]*X
    cnt = -1
    jump = 0
    for i in A:
        cnt += 1
        if leaf[i-1] == False:
            leaf[i-1] = True
            jump += 1
        if jump == X:
            return cnt
    return -1
    pass

# 48%


def solution(X, A):
    leaf = [False]*X
    cnt = -1
    for i in A:
        cnt += 1
        if leaf[i-1] == False:
            leaf[i-1] = True
        if False not in leaf[0:X]:
            return cnt
    return -1
    pass
