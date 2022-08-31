"""
    유클리드 호제법
    - 최대공약수를 구하는 방법
    - 이를 응용해 최소 공배수도 구할 수 있다
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 유클리드 호제법
def gcd(a,b):
    while(b != 0):
        n = a % b
        a = b
        b = n
    return a

# 재귀를 이용한 방법
def gcd_recursion(a,b):
    n = b % a
    if n == 0:
        return a
    return gcd_recursion(n,a)

num = gcd(max(n,m), min(n,m))
print(num) # 최대 공약수
print(n * m // num) # 최소 공배수