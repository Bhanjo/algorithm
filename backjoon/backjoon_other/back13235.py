import sys
input = sys.stdin.readline

word = str(input().strip())
i = 0
j = len(word)-1
result = "true"
while i <= j:
    if word[i] != word[j]:
        result = "false"
        break
    i += 1
    j -= 1
print(result)
