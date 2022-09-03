import sys
input = sys.stdin.readline

word = input().strip()
pattern = input().strip()

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
                answer.append(j-i+1)
                i = table[i-1]
                break # 다 확인할 필요 없이 하나만 존재하면 됨
    
    return answer

ans = kmp(word, pattern)
print(1 if len(ans) >= 1 else 0)


# 풀이2
# if pattern in word:
#     print(1)
# else:
#     print(0)