import sys
import heapq
input = sys.stdin.readline

# 동기화
def sync(hp):
    # heap이 존재, 맨 앞 id가 True일 때, pop을 해서 동기화
    while hp and not id[hp[0][1]]:
        heapq.heappop(hp)
        print(hp)

tc = int(input())
for t in range(tc):
    n = int(input())
    minH = []
    maxH = []
    id = [False] * 1000001 # 동기화

    for i in range(n):
        mode, num = map(str, input().strip().split())
        if mode == 'I':
            # value, id 튜플로 넣기
            id[i] = True
            heapq.heappush(minH, (int(num),i))
            heapq.heappush(maxH, (-int(num),i))
        elif mode == 'D':
            if num == '-1':
                sync(minH)
                if minH:
                    # 삭제처리, 해당 id를 False로
                    id[minH[0][1]] = False
                    heapq.heappop(minH)
            else:
                sync(maxH)
                if maxH:
                    id[maxH[0][1]] = False
                    heapq.heappop(maxH)

    sync(minH)
    sync(maxH)

    if minH and maxH:
        print(-1 * maxH[0][0], minH[0][0])
    else:
        print("EMPTY")