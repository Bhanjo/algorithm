import sys
input = sys.stdin.readline

s = int(input())
hap, cnt = 0, 0
while(hap < s):
    cnt += 1
    hap += cnt
    if hap > s:
        cnt -= 1
        break
print(cnt)