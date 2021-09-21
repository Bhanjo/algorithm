import sys
input = sys.stdin.readline

k, n = map(int, input().split())

cable = []
for _ in range(k):
    cable.append(int(input()))

cm = 1 #  start
max_cable = max(cable) # end

while(cm <= max_cable):
    mid = (cm + max_cable) // 2 # mid
    hap = 0

    for i in cable:
        hap += i // mid

    if hap >= n:
        cm = mid + 1
    else:
        max_cable = mid - 1

print(max_cable)
