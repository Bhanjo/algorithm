import sys
import re
input = sys.stdin.readline

start_words = ["c'", "j'", "n'", "m'", "t'", "s'", "l'", "d'", "qu'"]
moeum = ['a', 'e', 'i', 'o', 'u', 'h']
cnt = 0

words = input().strip()
split_words = re.split("-| ", words)  # 내장함수로 두 가지 경우의 split 실행(띄어쓰기와 하이픈)
for i in split_words:
    cnt += 1
    if i[0:3] in start_words or i[0:2] in start_words:  # 앞에 단어가 조건에 만족하는지 판단
        index = i.index("'")
        if i[index+1] in moeum:  # 작은따옴표 뒤 모음판단
            cnt += 1
print(cnt)
