"""
    위상정렬
    - 사이클이 없는 방향 그래프여야 한다
    - '사이클이 없는 방향 그래프'의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열한 것
    - 대표적으로 선수과목을 고려한 학습 순서가 있음
        - a->b, a->c, b->c 일 때, a->b->c 가능, a->c->b 불가
    - 진입차수 화살표를 받는 것, 진출차수 화살표를 보내는 것

    동작과정
    - 큐를 이용
    - 진입차수 0인 모든 노드를 큐에 넣기
    - while(q) => 큐 pop => pop한 노드에서 나가는 간선을 그래프에서 제거
    - 새롭게 진입차수가 0인 노드를 큐에 넣기 (순서 상관 없음)

    특징
    - 여러 답이 존재 가능 => 한 단계에서 큐에 들어가는 순서에 따라 달라짐
    - 모든 원소 방문 전 큐가 빈다 => 사이클 존재
    - DFS로 위상 정렬 가능
"""

# 예시 (백준 2252번 유사)
from collections import deque

v, e = map(int, input().split())

indegree = [0] * (v+1) # 노드에 대한 진입 차수
graph = [[] for _ in range(v+1)]

for i in range(e):
    a, b = map(int(input().split()))
    graph[a].append(b)
    indegree[b] += 1 # 진입차수 1증가

def topologySort(): # 위상 정렬
    answer = []
    q = deque()

    # 진입차수가 0인 노드들 추가
    for i in range(v):
        if indegree[i] == 0:
            q.append(i)
    
    while(q):
        node = q.popleft()
        answer.append(node)
        # node와 연결된 노드들의 진입 차수 감소
        for i in graph[node]:
            indegree[i] -= 1
            # 진입차수가 새롭게 0이 됐다면 큐에 추가
            if indegree[i] == 0:
                q.append(i)
    
    for i in answer:
        print(i)

topologySort()