n, m = map(int, input().split())
num_list = [1 + i for i in range(n)]
num_check = [False]*n
arr = []

def DFS(x):
    if x == m:
        print(*arr)
    
    for i in range(n):
        if num_check[i]:
            continue
        arr.append(num_list[i])
        num_check[i] = True
        DFS(x+1)
        arr.pop()
        # num_check[i] = False
        # print("num: ", arr)
        for j in range(i + 1, n):
            num_check[j] = False
        # print("체크", num_check)

DFS(0)

