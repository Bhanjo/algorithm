import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

left = 0
right = max(nums)
answer = right

def divSearch(mid):
    global answer
    minVal, maxVal = nums[0], nums[0]
    div = 1 # 아무것도 안 자르면 배열은 1개이기 때문

    # 투 포인터로 최대 최소 구하고 판별
    for i in nums:
        if i > maxVal:
            maxVal = i
        if i < minVal:
            minVal = i
        # 구간 나누기
        if maxVal - minVal > mid:
            # i 기준으로 두 개로 분리 (구간 생성)
            div += 1
            # i를 시작 인덱스로 지정
            minVal = i
            maxVal = i
    
    # 정해진 구간 이하로 나눌 수 있을 때
    return m >= div

while(left <= right):
    mid = (left + right) // 2
    isValid = divSearch(mid)

    # m개 이하로 나눌 수 있는지 판별
    if isValid:
        # 값이 '최소'인 것을 골라야함, mid로 m개 이하로 나눌 수 있으면 더 작은 값으로 시도해보기
        right = mid - 1
        answer = min(answer, mid)
    else:
        left = mid + 1

print(answer)