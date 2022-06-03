import sys
input = sys.stdin.readline

tc = int(input())

for t in range(tc):
    M,N,X,Y = map(int, input().split())
    while(X <= M*N):
        if (X-Y) % N == 0:
            print(X)
            break
        X += M
    if X > M*N:
        print(-1)