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


"""
    크루스칼 알고리즘 일반적 방법
    - union-find 알고리즘 사용

    union-find 알고리즘
    - 노드간의 연결 관계 파악 시 사용
    - parent 배열 각 요소에 해당 인덱스 번호 노드의 부모 노드 번호를 저장한다
        - [0,1,0,1,1] => 1번-3번, 1번-4번, 0번-2번 으로 연결되어 있다. (부모는 0번, 1번)
        - 배열의 초기값은 해당 인덱스 번호다 => [0,1,2,3,4,...,n-1]
    - find 함수
        - 루트 노드를 찾는 연산, 재귀를 이용
        - 부모[node] == node && 루트노드를 의미, return
        - 부모[node] != node && 부모가 존재 => 재귀를 통해 부모의 부모 찾기 => find(parent[node])
        - 시간복잡도 최소화를 위해 경로 압축 최적화 가능
    - union 함수
        - 서로 다른 부모를 가진 노드를 하나의 부모를 가지도록 합치는 과정
        - find 함수가 필수적으로 필요
        - node1, node2의 부모를 찾기 (p1, p2라 가정)
        - (p1 > p2)? parent[p2] = p1 : parent[p1] = p2
        - 즉, 번호가 더 큰 부모가 번호가 작은 노드의 자식으로 들어감

"""

# 백준 1197번
n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
graph.sort(key=lambda x:x[2])
answer = 0

# union-find 부모 노드 번호 보관할 배열, 초기값은 자기 자신이다
parent = [i for i in range(n+1)]

def find(x):
    # 부모가 자기 자신 => root 의미 => 그대로 넘겨주기
    if parent[x] == x:
        return x
    
    # 경로 압축 최적화 (선택사항)
    parent[x] = find(parent[x])

    # 부모 찾기 위해 거슬러 올라가기
    return find(parent[x])

def union(x,y):
    # x,y의 부모 찾기
    parentX, parentY = find(x), find(y)
    
    # 큰 노드의 부모를 작은 노드로 갱신
    if parentX > parentY:
        parent[parentX] = parentY
    else:
        parent[parentY] = parentX

for a,b,cost in graph:
    # 서로 같은 부모 => 사이클 생성 가능성 존재 => 건너뜀
    if find(a) == find(b):
        continue
    
    # a,b의 부모를 같은것으로 만들고 비용 갱신
    union(a,b)
    answer += cost

print(answer)