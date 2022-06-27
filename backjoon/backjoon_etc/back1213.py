import sys
from collections import Counter
input = sys.stdin.readline

word = list(map(str, input().strip()))
word.sort()
wordCount = Counter(word) # 단어 등장 횟수 카운트

oddCount = 0
centerWord = ''

for i in wordCount:
    if wordCount[i] % 2 != 0:
        oddCount += 1
        centerWord += i
        word.remove(i)
    if oddCount > 1: # 홀수 개수가 1개 초과라면 펠린드롬 만들지 못함
        break

ans = ''
for i in range(0, len(word), 2):
    ans += word[i]

# ans[::-1] 왼쪽->오른쪽으로 읽기 (reverse)
print(ans+centerWord+ans[::-1] if oddCount <= 1 else "I'm Sorry Hansoo")