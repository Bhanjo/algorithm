"""
    크루스칼 알고리즘
    - 그리디 알고리즘 응용
    - 모든 정점을 '최소'로 연결하는 최적의 해답을 구하는 것
    
    핵심
    - 사이클이 생성되지 '않는다'

    동작
    - 그래프 간선을 가중치의 '오름차순'으로 정렬
    - 간선 리스트에서 사이클을 형성하지 않는 간선 선택
        - 즉, 가중치가 가장 낮은 가중치 선택
        - 사이클을 형성하는 간선은 제외
    - 해당 간선을 현재의 MST(최소 비용 신장 트리)의 집합에 추가

    주의 (사이클 생성 판별)
    - 새로운 간선이 이미 연결된 정점을 연결한다 => 사이클 생성
        - 간선 = (a,b), 이미 연결된 것 = (a,g), (b,g)
        - (a,b)는 이미 연결된 것에 있음 => 사이클 생성
        - 즉, 새로운 간선의 두 정점이 집합에 속해있다 => 사이클 생성
    - 간선의 정점이 속해있는지 검사 => union-find 사용
"""

def solution(n, costs):
    answer = 0
    # 크루스칼 조건 = 가중치 기준 오름차순
    costs.sort(key=lambda x:x[2])
    # 연결된 노드들 보관, 가장 가중치가 작은 노드를 시작점으로
    nodes = set([costs[0][0]])

    # 크루스칼 알고리즘 실행 (모든 정점이 연결됐는가 판별)
    while(len(nodes) < n):
        for islandA, islandB, money in costs:
            # 간선의 두 정점이 이미 다른 것과 연결됨 => 사이클 발생
            if islandA in nodes and islandB in nodes:
                continue
            if islandA in nodes or islandB in nodes:
                nodes.update([islandA, islandB])
                answer += money
                break # len(nodes) < n 조건 초과를 방지하기 위함
    return answer