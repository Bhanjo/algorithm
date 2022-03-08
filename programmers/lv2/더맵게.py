import sys
import heapq as h
input = sys.stdin.readline

def solution(scoville, K):
  answer = 0
  h.heapify(scoville)

  while True:
    isPerfect = True
    for i in h:
      if(i < K):
        isPerfect = False
        break
    
    if isPerfect:
      return answer
    if isPerfect == False and len(h) < 2:
      return -1

    if isPerfect == False:
      if len(h) >= 2:
        food1 = h.heappop(h)
        food2 = h.heappop(h)
        newFood = food1 + (food2 * 2)
        h.heappush(h, newFood)
        answer += 1

print(solution([1, 2, 3, 9, 10, 12], 7))

# best
import heapq as hq
def solution(scoville, K):
    hq.heapify(scoville) # 배열을 heap으로 바꾸기
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K: # 가장 작은 값이 k 이상이면 모든 값이 k 이상이다
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer