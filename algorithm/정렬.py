# 예시: 백준 2693번
import sys
input = sys.stdin.readline

"""
    퀵 정렬 
    - O(nlogn)의 시간복잡도를 가짐
    - pivot을 기준으로 정렬 실행

    실행 과정
    - start >= end 이면 퀵 소트 종료
    - start = 보통 배열의 시작점, end = 가장 끝 원소의 인덱스
    - left = start + 1, right = end
    - left <= right 즉, 이 둘이 엇갈리지 않을 때 까지 진행
        - left의 idx 1씩 증가하며 pivot 보다 큰 값 찾기
        - right의 idx 1씩 감소하며 pivot 보다 작은 값 찾기
            - left, right를 찾았다면 이 둘을 swap
            - 만약, left > right 이라면 pivot과 right를 swap
    - right를 기준으로 두 개로 분할 후 재귀
"""
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

"""
    버블 정렬 
    - O(n**2)의 시간복잡도를 가짐

    실행 과정
    - 앞 값과 그 다음 값을 비교
    - 앞 값 > 다음 값 이라면, 이 둘을 swap
    - 한 번 순회시 가장 마지막에는 가장 큰 값이 들어감
        - 따라서 그 이후부터는 범위를 조금씩 좁혀갈 수 있음
"""
def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

"""
    삽입 정렬
    - O(n**2)의 시간복잡도를 가짐

    실행 과정
    - 새로운 값을 기존 값과 하나씩 비교
    - 앞 값 > 다음 값 이라면, 이 둘을 swap
    - 비교 범위가 점점 넓어짐
"""
def insertion_sort(nums):
    for end in range(1, len(nums)):
        for i in range(end, 0, -1):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]

"""
    선택 정렬
    - O(n**2)의 시간복잡도를 가짐

    실행 과정
    - idx를 순차적으로 선택
    - 해당 idx의 값보다 작은 값의 idx 선택 (minIdx)
    - 가장 작은 값 선택이 완료됐으면 minIdx 값과 idx의 값을 swap
    - 비교 범위가 점점 좁아짐
"""
def selection_sort(nums):
    for i in range(len(nums)-1):
        minIdx = i
        for j in range(i+1, len(nums)):
            if nums[minIdx] > nums[j]:
                minIdx = j
        nums[minIdx], nums[i] = nums[i], nums[minIdx]