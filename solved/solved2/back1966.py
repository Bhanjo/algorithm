t = int(input())

for _ in range(t):
    # n: 문서 개수, m: 알고싶은 m번째 문서, star: 중요도
    n, m = map(int, input().split())
    star = list(map(int, input().split()))
    index = [i for i in range(len(star))]
    index[m] = 'target'
    prt = 0

    while True:
        if star[0] == max(star):
            prt += 1
            if index[0] == 'target':
                break
            else:
                star.pop(0)
                index.pop(0)
        else:
            star.append(star.pop(0))
            index.append(index.pop(0))

    print(prt)