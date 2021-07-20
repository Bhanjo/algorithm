def myCode():
    xylist = []
    xylist.append(list(map(int, input().split())))
    xylist.append(list(map(int, input().split())))
    xylist.append(list(map(int, input().split())))

    x1 = (max(xylist[0][0],xylist[1][0],xylist[2][0]))
    x2 = (min(xylist[0][0],xylist[1][0],xylist[2][0]))

    y1 = (max(xylist[0][1],xylist[1][1],xylist[2][1]))
    y2 = (min(xylist[0][1],xylist[1][1],xylist[2][1]))

    cntX1 = 0
    cntX2 = 0
    cntY1 = 0
    cntY2 = 0

    for i in range(0, 3):
        if(xylist[i][0] == x1):
            cntX1 += 1
        else:
            cntX2 += 1
        if(xylist[i][1] == y1):
            cntY1 += 1
        else:
            cntY2 += 1

    if(cntX1 == 1):
        if(cntY1 == 1):
            print(x1, y1)
        else:
            print(x1, y2)
    else:
        if(cntY1 == 1):
            print(x2, y1)
        else:
            print(x2, y2)
        
def bestCode():
    xList = []
    yList = []
    for i in range(3):
            x, y = map(int, input().split())
            xList.append(x)
            yList.append(y)
    for i in range(3):
            if xList.count(xList[i]) == 1:
                    x = xList[i]
            if yList.count(yList[i]) == 1:
                    y = yList[i]
    print(x, y)

def main():
    myCode()
if __name__ == '__main__':
    main()