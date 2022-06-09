from itertools import permutations
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

# 라이브러리 풀이
# permu = list(permutations(nums, m))
# for i in permu:
#     for j in i:
#         print(j, end=' ')
#     print()

# 정석 풀이
ans = []
visit = [0 for _ in range(n)]
def permu(iter, n, m):
    if iter == m: # m까지 순회 시 출력
        print(' '.join(map(str, ans)))
        return
    for i in range(n):
        if visit[i] == 0:
            visit[i] = 1
            ans.append(nums[i]) # 출력할 숫자에 추가
            permu(iter + 1, n, m) # iter == m이 될때까지 재귀
            ans.pop() # 출력했으니 맨 뒤 숫자 pop
            visit[i] = 0

permu(0, n, m)