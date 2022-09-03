n, x = map(int, input().split())
a = list(map(int, input().split()))

for j in range(n) :
    if(a[j] < x) :
        print(a[j], end=' ')