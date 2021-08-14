n, m = map(int, input().split())
num_list = [i+1 for i in range(n)]
check_num = [False]*n
arr = []

def DFS(x):
    if x == m:
        print(*arr)
        return
    for i in range(n):
        arr.append(num_list[i])
        DFS(x + 1)
        arr.pop()

DFS(0)