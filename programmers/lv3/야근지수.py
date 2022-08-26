import heapq

# 가장 값이 높은 것을 떨어뜨려야 한다, 각 작업 비용은 1로 동일
# => 모든 작업을 동일하게 만들어야한다 => heap 이용
def solution(n, works):
    answer = 0
    h = []
    if sum(works) <= n:
        return answer
    
    for i in works:
        heapq.heappush(h, -i)
    
    for i in range(n):
        val = heapq.heappop(h) + 1
        heapq.heappush(h, val)
    
    while(h):
        val = -heapq.heappop(h)
        answer += val**2
    
    return answer