n = int(input())
en = input()

# 알파벳 소문자는 97~122
result = 0
for j in range(n):
    result += (ord(en[j])-96) * (31**j)
print(result % 1234567891)
