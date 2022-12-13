import sys
input = sys.stdin.readline

W, H, X, Y, P = map(int, input().split())
count = 0
for _ in range(P):
    x, y = map(int, input().split())
    
    if (X <= x <= X+W) and (Y <= y <= Y+H):
        count +=1
        continue
    
    R = H/2
    d1 = ((x-X)**2 + (y-(Y+R))**2)**0.5
    d2 = ((x-(X+W))**2 + (y-(Y+R))**2)**0.5
    if d1 <= R or d2 <= R:
        count += 1

print(count)
