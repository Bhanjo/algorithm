def sosu(num):
    if(num <= 1):
        return False
    else:
        for i in range(2, int(num**(1/2))+1):
            if(num % i == 0):
                return False
        return True

arr = list(range(2,246912))
arr_result = []

for i in arr:
    if(sosu(i)):
        arr_result.append(i)

a = int(input())

while(a != 0):
    cnt = 0
    for i in arr_result:
        if(a < i <= a*2):
            cnt += 1
    print(cnt)
    a = int(input())