def myCode():
    # x,y: 내 위치 / w,h: 사각형크기
    x,y,w,h = map(int,input().split())
    up = h - y
    down = y
    left = x
    right = w - x
    print(min(up, down, left, right))
def main():
    myCode()
if __name__ == '__main__':
    main()