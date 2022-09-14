def solution(gems):
    answer = [1,len(gems)]
    gemList = list(set(gems)) # 보석 종류
    jew = {gems[0]: 1} # 현재까지 쓸어간 보석들
    left,right = 0,0
    
    while left < len(gems) and right < len(gems):
        # 보석 종류가 부족하면 더 채우기
        if len(jew) < len(gemList):
            right += 1
            if right == len(gems):
                break
            rightGem = gems[right]
            
            if rightGem not in jew:
                jew[rightGem] = 1
            else:
                jew[rightGem] += 1
        else:
            # 충분하면 답 갱신
            if answer[1] - answer[0] > right - left:
                answer[0] = left + 1
                answer[1] = right + 1

            if jew[gems[left]] - 1 > 0:
                jew[gems[left]] -= 1
            else:
                del jew[gems[left]]
            left += 1
            
    return answer