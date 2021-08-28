n = int(input())
en = str(input())
hash = []
r = 31
m = 1234567891

# 알파벳 소문자는 97~122
# 부분성공 범위 1~50에서의 최적화 필요
for i in range(len(en)):
    hash.append(ord(en[i])-96)
result = 0
for j in range(n):
    result += hash[j] * (r**j) % m

print(result)
