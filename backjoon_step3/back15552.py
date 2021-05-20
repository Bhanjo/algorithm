import sys

inputNum = sys.stdin.readline
tc = int(inputNum())

for i in range(tc) :
    a,b = map(int,inputNum().split())
    print(a+b)