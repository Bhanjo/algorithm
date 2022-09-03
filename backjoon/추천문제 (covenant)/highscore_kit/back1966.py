from collections import deque
import sys
input = sys.stdin.readline

tc = int(input())

for t in range(tc):
    size, target = map(int,input().split())
    q = list(map(int, input().split()))

    for i in range(size):
       q[i]  = [i, q[i]] # [index, 중요도]
    
    q = deque(q)
    maxVal = max(q, key=lambda x:x[1])
    cnt = 1

    while(q):
        val = q.popleft()
        # 우선순위 낮음 => 맨 뒤에 추가 그 이후 건너뜀
        if val[1] < maxVal[1]:
            q.append(val)
            continue
        # 우선순위 같음, 타겟과 일치 => 출력
        if val[0] == target:
            print(cnt)
            break
        # 우선순위 같음 => 뽑은 횟수 증가, 뽑을 중요도 갱신
        cnt += 1
        maxVal = max(q, key=lambda x:x[1])