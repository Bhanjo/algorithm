import heapq

def solution(jobs):
    answer = 0
    now, i = 0,0 # 현재 시간, index
    start = -1 # 작업 시작 시간
    h = []
    
    while len(jobs) > i:
        for j in jobs:
            # 작업 시작시간과 현재 시간 사이에 노드들이 들어온 경우
            if start < j[0] <= now:
                heapq.heappush(h, [j[1], j[0]])
        if len(h) > 0: # 작업할 것이 있다면 작업
            currWork = heapq.heappop(h)
            start = now
            now += currWork[0]
            answer += now - currWork[1]
            i += 1
        else: # 없다면 현재 시간 증가
            now += 1
    return answer // len(jobs)