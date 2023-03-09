N = int(input())
H = list(map(int, input().split()))
result = [0] * N

for i in range(N):
    cnt_zero = 0

    for j in range(N):
        if cnt_zero == H[i] and result[j] == 0:
            result[j] = i + 1  # 수 1 ~ N
            break
        elif(result[j] == 0):
            cnt_zero += 1

print(*result)
