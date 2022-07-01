def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2 + 1):
        w = list(map(''.join, zip(*[iter(s)]*i)))
        if len(s) % i != 0 and s[i * len(w):] != '':
            w.append(s[i * len(w):])
        prevWord = w.pop(0)
        splitedWord = []
        cnt = 1
        while(w):
            currWord = w.pop(0)
            if prevWord == currWord:
                cnt += 1
            else:
                splitedWord.append(str(cnt) + prevWord if cnt > 1 else prevWord)
                cnt = 1
                
            if len(w) == 0:
                splitedWord.append(str(cnt) + currWord if cnt > 1 else currWord)
            prevWord = currWord
            
        zipWord = ''.join(splitedWord)
        answer = min(answer, len(zipWord))
    return answer

# 다른 풀이
def solution(s):
    answer = 10**10

    # 1부터 글자수 절반까지 압축 시도
    for i in range(1, len(s)//2+2):
        word = '' # 압축한 결과
        cnt = 1
        tempWord = s[:i] # 압축 후보
        # 끝까지 탐색
        for j in range(i, len(s)+i, i): # 끝 까지 압축 횟수만큼 증가하며 반복
            if tempWord == s[j:j+i]: # 압축 후보와 같음
                cnt += 1
            else:
                if cnt == 1: # 압축할 글자 없으면 그대로 붙이기
                    word += tempWord
                else:
                    word += str(cnt)+tempWord
                tempWord = s[j:j+i] # 압축 후보 갱신
                cnt = 1
        answer = min(answer, len(word))
    return answer
solution("abcabcabcabcdededededede")