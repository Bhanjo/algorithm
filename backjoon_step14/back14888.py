n = int(input())
num = list(map(int,input().split()))
op = list(map(int, input().split()))
hap = num[0]
maxhap = -1000000001
minhap = 1000000001

def dfs(cnt, hap, plus, minus, gop, nanum):
    global maxhap
    global minhap
    if cnt == n:
        maxhap = max(hap, maxhap)
        minhap = min(hap, minhap)
        return
    if plus:
        dfs(cnt + 1, hap + num[cnt], plus - 1, minus, gop, nanum)
    if minus:
        dfs(cnt + 1, hap - num[cnt], plus, minus - 1, gop, nanum)
    if gop:
        dfs(cnt + 1, hap * num[cnt], plus, minus, gop - 1, nanum)
    if nanum:
        dfs(cnt + 1, hap // num[cnt] if hap >= 0 else -(-hap // num[cnt]), plus, minus, gop, nanum - 1)

dfs(1, hap, op[0], op[1], op[2], op[3])
print(maxhap)
print(minhap)