# def myCode():
#     a,b = map(int, input().split())
    
#     num_list = [1 + i for i in range(a)] # 숫자 리스트 생성
#     check_num = [False]*a
#     arr = []

#     def DFS(x):
#         # 입력받은 숫자가 끝 까지 오게 된다면 출력
#         if x == b:
#             print(*arr)
        
#         for i in range(a):
#             if check_num[i]: # 이미 방문한 숫자라면 넘어감
#                 continue
#             # i를 배열에 추가 후 해당 위치 방문 표시
#             arr.append(num_list[i])
#             check_num[i] = True
            
#             DFS(x+1) # 다음 DFS 실행
#             arr.pop() # 조건이 True 되기 직전인 상태로 되돌림
#             check_num[i] = False # check 초기화
#     DFS(0)
# # testsetse
# def main():
#     myCode()
# if __name__ == '__main__':
#     main()

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visit = [False] * (n+1)

answer = []
arr = []
def dfs(visit, depth, currDepth):
    global arr
    if currDepth == depth:
        print(' '.join(map(str, arr)))
        answer.append(arr)
        return
    for i in range(1, n+1):
        if not visit[i]:
            visit[i] = True
            arr.append(i)
            dfs(visit, depth, currDepth + 1)
            visit[i] = False
            arr.pop()

dfs(visit, m, 0)
