import math

def myCode():
    a = int(input())
    print(f'{round(a*a*math.pi,6):.6f}')
    print(f'{round(a*a*2,6):.6f}')

def main():
    myCode()
if __name__ == '__main__':
    main()