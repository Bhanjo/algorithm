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
