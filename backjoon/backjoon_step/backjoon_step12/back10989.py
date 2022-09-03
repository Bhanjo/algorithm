import sys

def myCode():
    a = int(sys.stdin.readline())
    
    sort_list = [0]*(10001)
    for _ in range(a):
        a = int(sys.stdin.readline())
        sort_list[a] += 1

    for i in range(len(sort_list)):
        if(sort_list[i] != 0):
            for j in range(sort_list[i]):
                sys.stdout.write(str(i) + "\n")

def main():
    myCode()
if __name__ == '__main__':
    main()