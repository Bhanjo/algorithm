# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 개구리 위치 = X
# Y와 같거나 큰 거리만큼 움직이길 원함
# 개구리는 D만큼 고정된 거리를 움직일 수 있음

# Y에 가길 위한 최소한의 점프 횃수를 구해라
def solution(X, Y, D):
    distance = Y - X
    result = distance // D
    if distance % D > 1:
        result += 1
    return result
    pass
