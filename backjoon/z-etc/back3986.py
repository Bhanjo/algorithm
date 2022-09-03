import sys
input = sys.stdin.readline

n = int(input())
answer = 0

for i in range(n):
    word = list(input().strip())
    st = []
    for w in range(len(word)):
        if st and word[w] == st[-1]:
            st.pop()
        else:
            st.append(word[w])
    if not st:
        answer += 1
print(answer)