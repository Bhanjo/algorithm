import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def gcd(a,b):
    n = 0
    while(b != 0):
        n = a % b
        a = b
        b = n
    return a

num = gcd(max(n,m), min(n,m))
print(num)
print(n * m // num)