import sys
input = sys.stdin.readline

INF = 100000000
city = int(input())
bus = int(input())
graph = [[INF] * (city + 1) for _ in range(city + 1)]

for i in range(bus):
    start, end, cost = map(int, input().split())
    graph[start][end] = min(graph[start][end], cost)

for waypoint in range(city + 1):
    for go in range(city + 1):
        for to in range(city + 1):
            graph[go][to] = min(graph[go][to], graph[go][waypoint] + graph[waypoint][to])

for i in range(1, city + 1):
    graph[i][i] = 0
    cost = ''
    for j in range(1, city + 1):
        if graph[i][j] == INF:
            graph[i][j] = 0
        cost += str(graph[i][j])
        cost += ' '
    print(cost)