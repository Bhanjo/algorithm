import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
city = list(map(int, input().split()))

answer = 0
price = city[0]

for i in range(n - 1):
    answer += price * dist[i]
    price = min(price, city[i + 1])

print(answer)
