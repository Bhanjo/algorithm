wh = [0 for i in range(101)]
wh[1] = 1
wh[2] = 1
wh[3] = 1
for i in range(0, 98):
    wh[i + 3] = wh[i] + wh[i + 1]
t = int(input())
for i in range(t):
    n = int(input())
    print(wh[n])