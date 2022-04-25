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
def solition(s):
    answer = 10**5
    for i in range(1, len(s)//2+2):
        word = ''
        cnt = 1
        temp = s[:i]
        for j in range(i, len(s) + i, i):
            if temp == s[j:j+i]:
                cnt += 1
            else:
                if cnt == 1:
                    word += temp
                else:
                    word += (str(cnt) + temp)
                temp= s[j:j+i]
                cnt = 1
        answer = min(answer, len(word))
    return answer
solition("abcabcabcabcdededededede")