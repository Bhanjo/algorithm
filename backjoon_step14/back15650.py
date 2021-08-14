n, m = map(int, input().split())
num_list = [1 + i for i in range(n)]
num_check = [False]*n
arr = []

def DFS(x):
    if x == m:
        print(*arr)
    
    for i in range(n):
        if num_check[i]:
            # print(num_list[i],"는 중복입니다!")
            continue
        arr.append(num_list[i])
        num_check[i] = True
        DFS(x+1)
        arr.pop()
        # num_check[i] = False
        print("x는: ", x)
        
        # i 이후의 숫자만 체크를 풀게되면
        # i 이전 수들은 방문한 것으로 되니 출력이 안된다
        # ex) i = 1 일 때
        # [t, t, f, f]
        # 1~2는 방문 한 것으로 되어 3부터 출력됨
        for j in range(i + 1, n):
            num_check[j] = False
        print("check는: ", num_check)

DFS(0)

