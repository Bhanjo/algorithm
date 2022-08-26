def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2])
    nodes = set([costs[0][0]])

    while(len(nodes) < n):
        for islandA, islandB, money in costs:
            if islandA in nodes and islandB in nodes:
                continue
            if islandA in nodes or islandB in nodes:
                nodes.update([islandA, islandB])
                answer += money
                break
    return answer