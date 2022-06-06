from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
radder = [0 for _ in range(150)]
snake = [0 for _ in range(150)]
visit = [0 for _ in range(150)]
q = deque()
q.append((0, 1))

# 사다리, 뱀 입력
for i in range(N):
    start, end = map(int,input().split())
    radder[start] = end
for i in range(M):
    start, end = map(int,input().split())
    snake[start] = end

while(q):
    cnt, pos = q.popleft()
    if pos >= 100:
        print(cnt)
        break
    if visit[pos] == 0:
        visit[pos] = 1
        move = 0
        # 주사위 1 ~ 6까지 굴리기
        for i in range(1, 7):
            # 현위치 + 주사위 만큼 이동했을 때 이벤트
            if radder[pos + i] == 0 and snake[pos + i] == 0:
                move = pos + i
            elif radder[pos + i] != 0:
                q.append((cnt + 1, radder[pos + i]))
            elif snake[pos + i] != 0:
                q.append((cnt + 1, snake[pos + i]))
        q.append((cnt + 1, move))
