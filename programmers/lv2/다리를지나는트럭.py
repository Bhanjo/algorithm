def solution(bridge_length, weight, truck_weights):
  answer = 0
  q = [0] * bridge_length
  
  while(len(q) > 0):
    answer += 1
    q.pop(0)
    # 다리 길이 판단
    if(truck_weights):
      if(sum(q) + truck_weights[0] <= weight):
        q.append(truck_weights.pop(0))
      else:
        q.append(0)

  return answer

solution(100, 10000, [10000,10000])
# solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])