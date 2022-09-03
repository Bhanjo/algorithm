import sys
input = sys.stdin.readline

word = input().rstrip()
pattern = input().rstrip()

def pi(pattern):
    table = [0 for _ in range(len(pattern))]
    i = 0

    for j in range(1, len(pattern)):
        while i > 0 and pattern[i] != pattern[j]:
            i = table[i-1]
        if pattern[i] == pattern[j]:
            i += 1
            table[j] = i
    
    return table

def kmp(word, pattern):
    table = pi(pattern)
    i = 0
    answer = []
    
    for j in range(len(word)):
        while i > 0 and pattern[i] != word[j]:
            i = table[i-1]
        if pattern[i] == word[j]:
            i += 1
            if i == len(pattern):
                answer.append(j-i+2) # 위치를 0이 아닌 1부터 시작
                i = table[i-1]
    
    return answer

ans = kmp(word, pattern)
print(len(ans))
print(*ans)
