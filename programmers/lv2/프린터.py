import sys
input = sys.stdin.readline

def solution(priorities, location):
  popCnt = 0
  while(1):
    paper = priorities[0]
    del priorities[0]
    if(len(priorities) == 0):
      popCnt += 1
      break

    if(paper >= max(priorities)): # pop 연산
      popCnt += 1
      if(location == 0):
        break
    else: # 뒤로 보내기
      priorities.append(paper)
      if(location == 0):
        location = len(priorities)

    location -= 1
  return popCnt

# best
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
