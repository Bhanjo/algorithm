import sys
input = sys.stdin.readline

n, c = map(int, input().split())
msg = list(map(int, input().split()))
check_msg = list(i for i in msg)
dic_msg = dict()

for i in check_msg:
    dic_msg[i] = msg.count(i)
sort_msg = sorted(dic_msg.items(),reverse=True, key = lambda x:x[1])
result = []
for i in sort_msg:
    for j in range(i[1]):
        result.append(i[0])
print(*result)