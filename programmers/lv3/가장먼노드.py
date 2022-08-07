from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visit = [0 for _ in range(n+1)]
    
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    
    def bfs():
        q = deque()
        q.append(1)
        visit[1] = True
        while(q):
            node = q.popleft()
            for i in graph[node]:
                if visit[i] == 0:
                    visit[i] = visit[node] + 1
                    q.append(i)
    
    bfs()
    maxValue = max(visit)
    for i in visit:
        if i == maxValue:
            answer += 1
    
    return answer