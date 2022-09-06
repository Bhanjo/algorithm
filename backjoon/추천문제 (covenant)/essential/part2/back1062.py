import sys
input = sys.stdin.readline

n,k = map(int, input().split())

if k < 5:
    print(0)
    exit()
elif k == 26:
    print(n)
    exit()

answer = 0
words = [set(input().strip()) for _ in range(n)] # 각 word의 중복 제거 후 추가
alpha = [0 for _ in range(26)]

# 기본 알파벳은 항상 등장하므로 미리 체크
for w in ['a','c','i','n','t']:
    alpha[ord(w) - ord('a')] = 1

def permu(target, cnt):
    global answer

    # 공통 단어 제외한 나머지 만큼 체크했을 때 판별
    if cnt == k-5:
        wordCheck = 0
        # 중복 제거된 각 단어를 한 글자씩 비교
        for word in words:
            isCorrect = True
            for ap in word:
                if not alpha[ord(ap) - ord('a')]:
                    isCorrect = False
                    break
            if isCorrect:
                wordCheck += 1
        answer = max(answer, wordCheck)
        return
    
    for i in range(target, 26):
        if not alpha[i]:
            alpha[i] = 1
            permu(i, cnt + 1)
            alpha[i] = 0

permu(0,0)
print(answer)


# 2회차
from itertools import combinations
import sys
input = sys.stdin.readline

n,k = map(int, input().split())
answer = 0
words = []
base = ['a','n','t','i','c']

# 공통 단어 제거
for i in range(n):
    word = input().rstrip()
    for i in base:
        word = word.replace(i,'')
    words.append(word)

k -= 5
if k < 0:
    print(0)
else:
    alpha = []
    for word in words:
        if word == '': continue
        al = list(set(word))
        alpha.extend(al)
    alpha = list(set(alpha))
    combis = []
    
    # 남은 단어로 k-5길이의 조합 만들 수 있는지 확인 (만들 수 없으면 최대 길이로 만들기)
    if len(alpha) < k:
        combis.extend(list(combinations(alpha, len(alpha))))
    else:
        combis.extend(list(combinations(alpha, k)))

    # 조합의 요소로 단어 지우고 단어가 다 지워졌는지 판별
    for combi in combis:
        temp = 0
        for word in words:
            for c in combi:
                word = word.replace(c,'')
            if word == '':
                temp += 1
        answer = max(answer, temp)

    print(answer)