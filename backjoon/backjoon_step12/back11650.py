import sys

def myCode():
    a = int(sys.stdin.readline())
    num = []

    for _ in range(a):
        num.append(list(map(int, input().split())))
    
    temp = []
    for i in range(0, a-1):
        for j in range(i, a):
            if(num[i][0] >= num[j][0]):
                temp = num[i]
                num[i] = num[j]
                num[j] = temp

            if(num[i][0] == num[j][0]):
                if(num[i][1] >= num[j][1]):
                    temp = num[i]
                    num[i] = num[j]
                    num[j] = temp

    for i in range(len(num)):
        sys.stdout.write(str(num[i][0]) + " " + str(num[i][1]) + "\n")

def bestCode():
    a = int(sys.stdin.readline())
    num = []
    for _ in range(a):
        num.append(list(map(int, sys.stdin.readline().split())))
    
    sortNum = sorted(num)
    for i in range(len(num)):
        sys.stdout.write(str(sortNum[i][0]) + " " + str(sortNum[i][1]) + "\n")
    

def main():
    # myCode()
    bestCode()
if __name__ == '__main__':
    main()