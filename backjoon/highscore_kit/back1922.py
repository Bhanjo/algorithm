import sys
input = sys.stdin.readline

n =int(input())
m = int(input())

graph = []
answer = 0

# 그래프 설정
for i in range(m):
    candid = list(map(int, input().split()))
    graph.append(candid)

# 최소 비용을 위해 비용 기준 오름차순, set에는 시작 노드로 가장 최솟값 넣기
graph.sort(key=lambda x:x[2])
nodes = set([graph[0][0]])

while(len(nodes) < n):
    for start, end, cost in graph:
        # 두 정점이 이미 nodes 존재 => 사이클
        if start in nodes and end in nodes:
            continue
        if start in nodes or end in nodes:
            nodes.update([start,end])
            answer += cost
            break

print(answer)
            