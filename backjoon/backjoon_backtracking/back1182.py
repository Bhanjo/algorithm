import sys
input = sys.stdin.readline

n, s = map(int, input().split())
# 숫자 합 => 순서와 상관 없음 => sort로 정렬 후 target 보다 큰 값 선택되게 만들기
nums = list(map(int, input().split()))
nums.sort()
visit = [False for _ in range(n)]
temp = []
answer = 0

# 숫자는 반드시 한 번만 선택 => target으로 제한
def dfs(target):
    global answer
    # 배열 합이 s와 일치 판별, 종료조건 => 선택한 숫자 개수가 nums 이상일 때
    if len(temp) > 0 and sum(temp) == s:
        answer += 1
    if len(temp) >= n:
        return
    for i in range(target, len(nums)):
        # 방문 확인으로 중복 선택 방지
        if not visit[i]:
            visit[i] = True
            temp.append(nums[i])
            dfs(i)
            temp.pop()
            visit[i] = False

dfs(0)
print(answer)