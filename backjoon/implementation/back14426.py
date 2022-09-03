import sys
inpuit = sys.stdin.readline

n, m = map(int, input().split())
words = [input().strip() for _ in range(n)]

result = 0
for i in range(m):
    alphabet = input().strip()
    for j in words:
        if alphabet == str(j[0:len(alphabet)]):
            result += 1
            break
print(result)

# 방법2 이진탐색 (인덱스 에러)
# n, m = map(int, input().split())
# words = []
# alphabet = []
# for _ in range(n+m):
#     if _ < n:
#         words.append(input())
#     else:
#         alphabet.append(input())
# words.sort()

# result = 0
# for i in alphabet:
#     num = len(i)
#     start = 0
#     end = len(words)

#     while(start <= end):
#         mid = (start + end) // 2
#         if len(words[mid]) >= num:
#             if i == str(words[mid][0:num]):
#                 result += 1
#                 break
#             else:
#                 if i[0] <= words[mid][0]:
#                     end = mid - 1
#                 else:
#                     start = mid + 1

# print(result)
