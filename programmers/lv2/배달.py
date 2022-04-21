import heapq

def solution(N, road, K):
    answer = 0
    cost = [500001]* (N+1)
    cost[1] = 0
    graph = [[] for _ in range(N+1)]

    for i in road:
        graph[i[0]].append([i[1], i[2]])
        graph[i[1]].append([i[0], i[2]])

    def dijkstra(cost, graph):
        h = []
        heapq.heappush(h, [1,0])
        while h:
            nowNode, value = heapq.heappop(h)
            for nextNode, nextCost in graph[nowNode]:
                if value + nextCost < cost[nextNode]:
                    cost[nextNode] = value + nextCost
                    heapq.heappush(h, [nextNode, value + nextCost])

    dijkstra(cost, graph)

    for i in cost:
        if i <= K:
            answer += 1
    return answer

solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4)