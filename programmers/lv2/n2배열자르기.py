def solution(n, left, right):
    lists = []
    for i in range(left, right + 1):
        div = (i // n) + 1
        rest = (i % n) + 1
        lists.append(max(div, rest))

    return lists