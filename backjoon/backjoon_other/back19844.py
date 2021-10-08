import sys
import re
input = sys.stdin.readline

start_words = ["c'", "j'", "n'", "m'", "t'", "s'", "l'", "d'", "qu'"]
moeum = ['a', 'e', 'i', 'o', 'u', 'h']
cnt = 0

words = input().strip()
split_words = re.split("-| ", words)
for i in split_words:
    cnt += 1
    if i[0:3] in start_words or i[0:2] in start_words:
        index = i.index("'")
        if i[index+1] in moeum:
            cnt += 1
            i = re.split("'", i)
print(cnt)
