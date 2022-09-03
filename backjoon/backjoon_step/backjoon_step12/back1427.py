num = list(map(int, str(input())))
tmp = 0

for i in range(len(num) - 1):
    for j in range(i, len(num)):
        if(num[i] < num[j]):
            temp = num[i]
            num[i] = num[j]
            num[j] = temp

for k in num:
    print(k, end="")
    