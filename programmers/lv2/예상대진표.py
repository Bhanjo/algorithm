def solution(n,a,b):
    answer = 1
    nums = [i+1 for i in range(n)]
    A, B, round = a, b, 1
    isContinue = True
    while(isContinue):
        nextRound = []
        for i in range(0, len(nums), 2):
            if (nums[i] == A or nums[i] == B) and (nums[i+1] == A or nums[i+1] == B):
                answer = round
                isContinue = False
                break
            elif nums[i] == A:
                A = (A // 2) + 1
                nextRound.append(A)
            elif nums[i+1] == A:
                A = A // 2
                nextRound.append(A)
            elif nums[i] == B:
                B = B // 2 + 1
                nextRound.append(B)
            elif nums[i+1] == B:
                B = B // 2
                nextRound.append(B)
            else:
                nextRound.append(nums[i+1] // 2)
            # print(nums)

        nums = nextRound
        round += 1
        if isContinue == False:
            break
    return answer

# 다른 코드
def solution(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2
    return answer
    
solution(8,4,7)