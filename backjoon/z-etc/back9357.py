import sys
input = sys.stdin.readline

tc = int(input())
for t in range(tc):
    clothes = int(input())
    dict = {}
    answer = 1
    for i in range(clothes):
        name, part = map(str, input().split())
        if part not in dict:
            dict[part] = [name]
        else:
            dict[part].append(name)
    for k in dict:
        answer *= len(dict[k]) + 1
    print(answer - 1)