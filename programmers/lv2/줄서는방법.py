import math

def solution(n, k):
    answer = []
    nums = list(i for i in range(1, n+1))
    
    # n개의 수 중 앞자리가 1이 되는 경우 = (n-1)!
    # 이를 통해 n!이 아닌 (n-1)! 계산이 가능해짐
    while n != 0:
        # 자릿수를 바꾸기 위한 경우의 수
        temp = math.factorial(n-1)
        
        # index = k번째에서 자릿수 바꾸기
        # k번째 경우의 수 = k! = k * (k-1)!
        # 앞자리 1자리 고정 시키고 나머지의 경우의 수 = (k-1)!개
        # n일 때 index => k번째로 큰 순서의 값
        index = (k-1) // temp
        k = k % temp
        answer.append(nums.pop(index))
        n -= 1
    return answer