import sys
input = sys.stdin.readline

answer = 0
people = 0
for i in range(10):
    minus, plus = map(int, input().split())
    people += plus - minus
    answer = people if answer < people else answer

print(answer)