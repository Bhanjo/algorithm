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

# 2회차
from collections import deque
def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    visit = [0 for _ in range(n+1)]
    
    for i in edge:
        a, b = i[0], i[1]
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs(node):
        q = deque()
        q.append(node)
        visit[node] += 1
        
        while(q):
            parent = q.popleft()
            for child in graph[parent]:
                if visit[child] == 0:
                    visit[child] = visit[parent] + 1
                    q.append(child)
    
    bfs(1)
    return visit.count(max(visit))