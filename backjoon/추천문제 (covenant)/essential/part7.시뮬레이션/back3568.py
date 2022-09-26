from curses.ascii import isalpha
import sys
input = sys.stdin.readline

word = input().strip()
word = word.split(';')

temp = []
for i in word:
    s = i.split(', ')
    s2 = []
    for j in s:
        s2.extend(j.split(' '))
    while('' in s2):
        s2.remove('')
    temp.append(s2)

for var in temp:
    if len(var) == 0: continue
    ty = var[0]
    # 변수 하나씩 불러오기
    for i in range(1, len(var)):
        # 변수 뒤집기
        n = []
        t = list(var[i])
        while(t):
            j = t.pop()
            if j == '[':
                p = n.pop()
                n.append(j)
                n.append(p)
            elif isalpha(j):
                t.append(j)
                t = t[::-1]
                break
            else:
                n.append(j)
        
        n.append(' ')
        while(t):
            n.append(t.pop())
        n = ty + ''.join(n) + ';'
        
        print(n)
