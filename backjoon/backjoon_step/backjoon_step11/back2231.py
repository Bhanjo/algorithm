def myCode():
    a = int(input())
    goal = 1
    while(goal <= a):
        num = goal
        goallength = len(str(goal))
        nanum = 10
        hap = num
        for i in range(goallength + 1):
            hap += num%nanum
            num = num//nanum
        if(hap == a):
            print(goal)
            break
        goal += 1

    if(hap != a):
        print(0)

def bestCode():
    n = int(input())
    result = 0
    for i in range(1, n + 1):
        a = list(map(int, str(i)))
        result = i + sum(a)
        if(result == n):
            print(i)
            break
        if (i == n):
            print(0)

def main():
    # myCode()
    bestCode()
if __name__ == '__main__':
    main()