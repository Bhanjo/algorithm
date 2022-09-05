import sys
input = sys.stdin.readline

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
    
    # 경로 압축 최적화
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
print(parent)