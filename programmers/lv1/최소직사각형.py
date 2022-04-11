def solution(sizes):
    for i in range(len(sizes)):
        w = sizes[i][0]
        h = sizes[i][1]
        if w >= h:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
    wMax = 0
    hMax = 0
    for i in range(len(sizes)):
        wMax = max(sizes[i][0], wMax)
        hMax = max(sizes[i][1], hMax)
    return hMax * wMax