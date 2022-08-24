import sys
input = sys.stdin.readline

n = int(input())
tops = list(map(int,input().split()))
answer = []
st = [] # 요소 = [index, tops[index]]

for i in range(n):
    while(len(st) > 0):
        last = st[-1]
        if last[1] > tops[i]:
            answer.append(last[0]+1)
            st.append([i, tops[i]])
            break
        else:
            st.pop()
    if len(st) == 0:
        st.append([i, tops[i]])
        answer.append(0)

print(*answer)