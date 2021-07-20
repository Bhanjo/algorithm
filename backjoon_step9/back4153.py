def myCode():
    while(True):
        a = list(map(int, input().split()))
        if(a[0] == a[1] == a[2] == 0):
            break
        x = min(a)
        y = max(a)
        a.remove(x)
        a.remove(y)
        z = sum(a)
        if((x*x) + (z*z) == y*y):
            print('right')
        else:
            print('wrong')
        
def bestCode():
    while True:
        a = list(map(int, input().split()))
        max_num = max(a)
        if sum(a) == 0:
                break
        a.remove(max_num)
        if a[0] ** 2 + a[1] ** 2 == max_num ** 2:
            print('right')
        else:
            print('wrong')

def main():
    myCode()
if __name__ == '__main__':
    main()