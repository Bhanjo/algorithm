import sys
input = sys.stdin.readline

st = list(input().strip())
temp = []
n = int(input())
wordCnt = len(st)

for i in range(n):
    cmd = list(input().strip())
    if cmd[0] == 'L' and len(temp) < wordCnt:
        temp.append(st.pop())
    elif cmd[0] == 'D' and len(st) < wordCnt:
        st.append(temp.pop())
    elif cmd[0] == 'B' and len(st) > 0:
        st.pop()
        wordCnt -= 1
    elif cmd[0] == 'P':
        st.append(cmd[2])
        wordCnt += 1

temp.reverse()
st.extend(temp)
print(''.join(st))