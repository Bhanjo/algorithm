# 알고리즘 과목 5주차 과제, 숫자 재배치
import sys
input = sys.stdin.readline

A = [0, 3, -1, 2, 5, 9, 1000, 23, -2, -9, -8, 123, -123, 0]
# A = [5,-9, 9, 0, -8, 0, 123, -123]
i = 0
j = len(A) - 1
# mid = A[len(A) // 2]
# print('중간값', mid)

# cnt = 0
while(i <= j):
    if A[i] <= 0:
        i += 1
    elif A[j] > 0:
        j -= 1
    else:
        temp = 0
        temp = A[i]
        A[i] = A[j]
        A[j] = temp
        i += 1
        j -= 1
        # print('교체', A)

print(A)