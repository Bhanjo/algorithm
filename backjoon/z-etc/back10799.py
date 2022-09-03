from collections import deque
import sys
input = sys.stdin.readline

st = deque()
ans = 0

braket = list(input().strip())
prevBraket = ''
for i in braket:
    if i == '(':
        st.append('(')
    else:
        if prevBraket == '(':
            st.pop()
            ans += len(st)
        else:
            st.pop()
            ans += 1
    prevBraket = i
print(ans)
