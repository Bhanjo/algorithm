def palindromeCheck(word, left, right):
    temp = 0
    # 짝수 팰린드롬인지 홀수 팰린드롬인지 판별, 홀수면 가운데는 무조건 살음 => 길이 1부터 시작
    if right - left > 1:
        temp = 1
    
    # 팰린드롬 판별, (좌 == 우) => 팰린드롬 만족 => length 증가, 다음 위치 탐색
    while left >= 0 and right <= len(word)-1:
        if word[left] == word[right]:
            left -= 1
            right += 1
            temp += 2
        else:
            break
    
    return temp

def solution(s):
    answer = 0
    if s == s[::-1] or len(s) == 1:
        return len(s)
    
    # 핵심 팰린드롬 최대 => aba => 좌우 추가 => cabac가 된다는 특성 이용
    for i in range(len(s)-1):
        answer = max(answer, palindromeCheck(s, i, i+1), palindromeCheck(s, i, i+2))
    return answer


# 복습
answer = 1

def pallin(word, idx, type):
    global answer
    cnt = 1 # 길이
    left = idx - 1
    right = idx + 1
    
    if type == 'even':
        if word[idx] != word[idx+1]:
            return
        cnt = 2
        right += 1
    
    
    while(left >= 0 and right < len(word)):
        if word[left] == word[right]:
            cnt += 2
            left -= 1
            right += 1
            answer = max(answer, cnt)
        else:
            break
    

def solution(s):
    global answer
    
    if len(s) == 1:
        return 1
    
    for i in range(1, len(s)-1):
        pallin(s, i, 'even')
        pallin(s, i, 'odd')

    return answer