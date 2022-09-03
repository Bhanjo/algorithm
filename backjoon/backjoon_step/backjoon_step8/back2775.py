def myCode():
    tc = int(input())
    for _ in range(tc):
        k = int(input())
        n = int(input())
        
        zero = [i for i in range(1, n+1)]
        for i in range(k):
            for j in range(1, n):
                zero[j] += zero[j - 1]
        print(zero[-1])

def main():
    myCode()
if __name__ == '__main__':
    main()