import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]
min_time = 9999999999
height = 0

for i in range(257):
    bottom = 0
    top = 0
    # 0층부터 256층까지 모든 땅을 i층으로 고르는 경우의 수를 다 구함
    for j in range(N):
        for k in range(M):
            if ground[j][k] >= i:
                top += ground[j][k]-i
            else:
                bottom += i-ground[j][k]

    # 채워야하는 블록이 가진 블록보다 많을 때
    # 즉, 땅을 평평하게 할 수 없을때 해당 건은 건너뛴다
    if bottom > top + B:
        continue

    # 채우기는 +1, 쌓기는 +2
    time = bottom + (top*2)
    if time <= min_time:
        min_time = time
        height = i

print(min_time, height)
