# math 모듈의 factorial 사용하여 풀 수 있음
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

def facto(x):
    hap = 1
    for i in range(1,x+1):
        hap *= i
    return hap

child = facto(n)
parant1 = facto(k)
parant2 = facto(n-k)
print(child//(parant1*parant2))