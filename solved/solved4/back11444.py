import sys
input = sys.stdin.readline

n = int(input())
graph = [[1,1],[1,0]]

# x*x
def calcEven(graph):
    tempGraph = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                tempGraph[i][j] += graph[i][k] * graph[k][j]
            tempGraph[i][j] %= 1000000007
    return tempGraph

# x*x*graph
def calcOdd(graph):
    tempGraph = [[0,0],[0,0]]
    originGraph = [[1,1],[1,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                tempGraph[i][j] += graph[i][k] * graph[k][j]
            tempGraph[i][j] %= 1000000007

    ansGraph = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                ansGraph[i][j] += tempGraph[i][k] * originGraph[k][j]
            ansGraph[i][j] %= 1000000007
    
    return ansGraph

def divcon(graph, n):
    if n == 1:
        return graph
    else:
        x = divcon(graph, n // 2)
        if n % 2 == 0:
            return calcEven(x)
        else:
            return calcOdd(x)

answer = divcon(graph, n)
print(answer[0][1] % 1000000007)