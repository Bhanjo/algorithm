def myCode():
    fix_money, move_money, price = map(int,input().split())
    point = 0

    if(move_money >= price):
       point = -1
    else:
        point = (fix_money / (price - move_money)) + 1

    print(int(point))

def main():
    myCode()
if __name__ == '__main__':
    main()