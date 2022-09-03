# 실패(다시 도전 필요)
import sys
input = sys.stdin.readline

n = int(input())
check_num = [False]*n
n_list = [i+1 for i in range(n)]

status = []
min_hap = []
# for i in range(n):
#     status.append(list(map(int,input().split())))

def dfs(x):
    if x == n//2:
        print(status)
        return
    for i in range(n):
        if check_num[i] == True:
            continue
        check_num[i] = True
        status.append(n_list[i])
        dfs(x+1)
        check_num[i] = False
        status.pop()
dfs(0)