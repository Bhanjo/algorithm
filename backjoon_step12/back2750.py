a = int(input())
num = []
for _ in range(a):
    num.append(int(input()))

temp = 0
for i in range(a):
    for j in range(a):
        if(num[i] < num[j]):
            temp = num[i]
            num[i] = num[j]
            num[j] = temp

for i in num:
    print(i)