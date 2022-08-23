#  100 / 100
def solution(a, b, n):
    answer = 0
    etc = 0
    while(n >= a):
        answer += (n // a)*b
        etc = n % a
        cola = (n // a) * b
        n = cola + etc
    return answer

# 2회차 (100)
def solution(a, b, n):
    answer = 0
    while(n >= a):
        change = (n // a) * b
        answer += change
        n = change + (n % a)
    return answer