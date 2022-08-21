def solution(numbers):
    arr = list(map(str,numbers))
    arr.sort(key=lambda x:x*3, reverse = True)
    return str(int(''.join(arr)))

# 2회차
import functools

def comp(x,y):
    # '3', '30'을 문자열 이어붙임으로 비교해 내림차순 정렬
    if x+y > y+x:
        return -1
    else:
        return 1

def solution(numbers):
    numbers = list(map(str, numbers))
    # functools의 key 비교 함수 이용
    answer = sorted(numbers, key=functools.cmp_to_key(comp))
    # 03과 같이 필요없는 '0'이 포함되는 것을 막기 위해 int->str 재변환
    return str(int(''.join(answer)))

solution([9,938])