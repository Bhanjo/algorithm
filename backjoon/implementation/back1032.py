import sys
input = sys.stdin.readline

answer = []
tc = int(input())
words = []

# 명령어 입력
for i in range(tc):
    words.append(input().strip())

targetWord = list(words[0])
for i in range(len(words[0])):
    currWord = targetWord[i]
    isCorrect = True
    for j in range(1, len(words)):
        if words[j][i] != currWord:
            isCorrect = False
            break
    answer.append(currWord if isCorrect else '?')

print(''.join(answer))