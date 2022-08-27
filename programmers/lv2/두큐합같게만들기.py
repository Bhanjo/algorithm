from collections import deque
def solution(queue1, queue2):
    answer = -1
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    maxLimit = len(queue1)+len(queue2)+100
    
    cnt = 0
    while(cnt < maxLimit):
        val = 0
        if sum1 > sum2:
            val = queue1.popleft()
            queue2.append(val)
            sum1 -= val
            sum2 += val
        elif sum1 < sum2:
            val = queue2.popleft()
            queue1.append(val)
            sum1 += val
            sum2 -= val
        else:
            answer = cnt
            break
        cnt += 1
    return answer