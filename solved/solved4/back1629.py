import sys
input = sys.stdin.readline

a, b, c = map(int,input().split())

# 나머지 분배 법칙 이용 (A*B)%C = (A%C)*(B%C)%C
def divcon(a,b):
    if b == 1:
        return a % c
    hap = divcon(a, b//2) # hap = (A%C) 혹은 (B%C)
    if b % 2 == 0: # 짝수일 때는 나머지 분배 법칙 그대로 적용
        return (hap*hap) % c
    else: # 홀수일 때는 a 추가 곱셈
        return (hap*hap*a) % c

print(divcon(a,b))