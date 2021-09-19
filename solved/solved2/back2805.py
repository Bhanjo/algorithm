import sys
input = sys.stdin.readline

n,m = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)

while start <= end:
    hap = 0
    mid = (start+end) // 2

    for i in tree:
        hap += i - mid if i > mid else 0
    
    if hap >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)