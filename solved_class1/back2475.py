num = list(map(int, input().split()))
hap = []
for i in num:
    hap.append(i*i)
print(sum(hap) % 10)