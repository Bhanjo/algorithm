import sys
input = sys.stdin.readline

n, k = map(int,input().split())
temp = list(map(int, input().split()))
hap = sum(temp[:k])
hapList = [hap]

for i in range(len(temp)-k):
    hap = hap - temp[i] + temp[i+k]
    hapList.append(hap)
    
print(max(hapList))