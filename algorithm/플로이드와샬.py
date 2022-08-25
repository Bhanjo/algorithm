"""
    플로이드 와샬 (예제 백준 11404번)
    - O(n**3) 소요
    - 다이나믹 프로그래밍의 응용

    핵심
    - '거쳐가는 정점'을 기준으로 알고리즘 수행
    
    다익스트라와 차이점
    - 모든 정점에서 모든 정점으로의 최단거리를 구할 때 사용
    - 다익스트라는 가장 적은 비용을 하나씩 선택
"""

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = 10**8
cost = [[INF]*n for _ in range(n)]

for i in range(m):
    start, end, dist = map(int, input().split())
    # 시작->도착 연결하는 노선은 하나가 아닐 수 있다 => (3->5 = 1), (3->5 = 10) 중 작은 값 넣기 위해
    cost[start-1][end-1] = min(cost[start-1][end-1], dist)

for i in range(n):
    cost[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

for i in cost:
    for j in i:
        if j == INF: # 갈 수 없는 경우 => 0으로 치환
            print(0, end=' ')
        else:
            print(j, end=' ')
    print('')