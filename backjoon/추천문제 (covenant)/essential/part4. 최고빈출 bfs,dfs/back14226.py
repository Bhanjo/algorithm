from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

def bfs():
    q = deque()
    q.append([1,0,0]) # 화면,보드,시간
    visit = [[False]*1001 for _ in range(1001)]
    
    while(q):
        view,board,time = q.popleft()
        if view == n:
            return time
        if 0 <= view+board <= 1000 and not visit[view][board]:
            visit[view][board] = True
            if 0 <= view <= 1000: # 화면에 있는거 모두 보드에 저장
                q.append([view,view,time+1])
            if 1 <= board <= 1000: # 보드에 있는거 모두 화면에 붙여넣기
                q.append([view+board,board,time+1])
            if 1 <= view <= 1000: # 화면에서 하나 삭제
                q.append([view-1,board,time+1])
print(bfs())