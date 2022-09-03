# 유니온파인드
import sys
input = sys.stdin.readline

tc = int(input())

def find(node):
    # node가 root인지 판별
    if node == friend[node]:
        return node
    else:
        # root를 찾기 위해 node의 부모로 거슬러 올라가기
        root = find(friend[node])
        # node의 부모를 root로 갱신
        friend[node] = root
        return friend[node]

def union(nodeA,nodeB):
    rootA, rootB = find(nodeA), find(nodeB)
    
    # nodeA와 nodeB의 부모가 같지 않으면
    if rootA != rootB:
        # nodeB의 부모를 nodeA의 부모로 바꾸기
        friend[rootB] = rootA
        # nodeA의 관계에 rootB 관계 추가
        nums[rootA] += nums[rootB]

for t in range(tc):
    friend = dict()
    nums = dict()
    lines = int(input())
    for i in range(lines):
        a, b = map(str, input().strip().split())

        if a not in friend:
            friend[a] = a
            nums[a] = 1
        if b not in friend:
            friend[b] = b
            nums[b] = 1

        # UnionFind 실행
        union(a,b)
        # a에 대한 부모를 찾고 부모가 가진 네트워크 수 출력
        print(nums[friend[a]])
        