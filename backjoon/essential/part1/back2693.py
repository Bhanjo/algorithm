import sys
input = sys.stdin.readline

tc = int(input())

# 퀵 정렬
def quick_sort(nums, start, end):
    # 종료 조건
    if start >= end:
        return
    
    # 기준 만들기
    pivot = start
    left = start + 1
    right = end

    # 정렬
    while left <= right:
        # 왼쪽 타겟 찾기 (피벗보다 큰 값의 인덱스 찾기)
        while left <= end and nums[left] <= nums[pivot]:
            left += 1
        # 오른쪽 타겟 찾기 (피벗보다 작은 값의 인덱스 찾기)
        while right > start and nums[right] >= nums[pivot]:
            right -= 1
        # swap
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
        else:
            nums[pivot], nums[right] = nums[right], nums[pivot]
    
    # 분할 정복 (새로운 피벗 인덱스 기준으로 좌, 우 나누기)
    quick_sort(nums, start, right - 1)
    quick_sort(nums, right + 1, end)

for t in range(tc):
    nums = list(map(int, input().split()))
    quick_sort(nums, 0, len(nums)-1)
    print(nums[len(nums)-3])