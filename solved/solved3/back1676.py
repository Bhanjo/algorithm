import sys
input = sys.stdin.readline

n = int(input())
hap = 1
while(n >= 2):
    hap *= n
    n -= 1
hap = str(hap)

i, cnt = len(hap)-1, 0
while(True):
    if hap[i] == '0':
        cnt += 1
    else:
        break
    i -= 1
print(hap)
print(cnt)
