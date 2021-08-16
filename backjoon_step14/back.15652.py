n, m = map(int, input().split())
check_num = [False]*n
num_list = [1 + i for i in range(n)]
arr = []

def DFS(x):
    if x == m:
        print(*arr)
        return
    for i in range(n):
        if check_num[i]:
            continue
        arr.append(num_list[i])
        DFS(x+1)
        check_num[i] = True
        arr.pop()
        for j in range(i+1, n):
            check_num[j] = False

DFS(0)