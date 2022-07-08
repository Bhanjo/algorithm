def hanoi(answer, n, fromNode, toNode, assistNode):
    if n == 1:
        answer.append([fromNode,toNode])
        return
    hanoi(answer, n-1, fromNode, assistNode, toNode)
    answer.append([fromNode,toNode])
    hanoi(answer, n-1, assistNode, toNode, fromNode)

def solution(n):
    answer = []
    hanoi(answer, n, 1,3,2)
    return answer