# 100/100
from collections import deque

def solution(topping):
    topping = deque(topping)
    answer = 0

    arr1 = dict()
    arr1Items = 0

    arr2 = dict()
    for i in topping:
        if i not in arr2:
            arr2[i] = 1
        else:
            arr2[i] += 1
    arr2Items = len(arr2)

    while(topping):
        t = topping.popleft()
        if arr2[t] > 0:
            arr2[t] -= 1
        if arr2[t] <= 0:
            arr2Items -= 1

        if t not in arr1:
            arr1[t] = 1
            arr1Items += 1
        
        if arr1Items == arr2Items:
            answer += 1
    return answer

# 2회차 (100/100)
from collections import deque
def solution(topping):
    answer = 0
    a = dict()
    b = dict()
    topping = deque(topping)

    # 형 딕셔너리 갱신
    aCnt = 0 # 딕셔너리 key 개수
    for i in topping:
        if i not in a:
            a[i] = 1
            aCnt += 1
        else:
            a[i] += 1

    
    # 동생에게 하나씩 넘기고 판단
    bCnt = 0
    for i in topping:
        a[i] -= 1
        if a[i] <= 0:
            aCnt -= 1
        if i not in b:
            b[i] = 1
            bCnt += 1
        else:
            b[i] += 1
        if aCnt == bCnt:
            answer += 1
    
    return answer