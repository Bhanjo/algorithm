import sys
input = sys.stdin.readline

dp = [[[0]*51 for _ in range(51)] for __ in range(51)]

def recur(x,y,z):
    if x <= 0 or y <= 0 or z <= 0:
        return 1
    if x > 20 or y > 20 or z > 20:
        return recur(20,20,20)
    if dp[x][y][z] != 0:
        return dp[x][y][z]
    if x < y < z:
        dp[x][y][z] = recur(x,y,z-1) + recur(x,y-1,z-1) - recur(x,y-1,z)
        return dp[x][y][z]
    dp[x][y][z] = recur(x-1,y,z) + recur(x-1,y-1,z) + recur(x-1,y,z-1) - recur(x-1,y-1,z-1)
    return dp[x][y][z]

while(True):
    x,y,z = map(int,input().split())
    if x == -1 and y ==-1 and z ==-1:
        break
    print(f'w({x}, {y}, {z}) = {recur(x,y,z)}')