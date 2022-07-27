import sys
input = sys.stdin.readline

n = int(input())
graph = [[1,1],[1,0]]

# x*x
def calcEven(a,b):
    tempGraph = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                tempGraph[i][j] += a[i][k] * b[k][j]
            tempGraph[i][j] %= 1000000007
    return tempGraph

def divcon(graph, n):
    if n == 1:
        return graph
    else:
        x = divcon(graph, n // 2)
        if n % 2 == 0:
            return calcEven(x,x)
        else:
            return calcEven(calcEven(x,x), graph)

answer = divcon(graph, n)
print(answer[0][1] % 1000000007)