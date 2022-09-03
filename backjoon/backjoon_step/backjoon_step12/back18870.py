import sys
def myCode():
    t = int(sys.stdin.readline())
    num = list(map(int, sys.stdin.readline().split()))
    num_cnt = [0]*t
    
    copy_num = list(set(num))
    for i in range(t):
        num_check = []
        for j in range(len(copy_num)):
            if num[i] > copy_num[j] and copy_num[j] not in num_check:
                num_cnt[i] += 1
                num_check.append(copy_num[j])

    for i in range(len(num_cnt)):
        if i == len(num_cnt)-1:
            sys.stdout.write(str(num_cnt[i]))
        else:
            sys.stdout.write(str(num_cnt[i]) + " ")
            
def bestCode():
    t = sys.stdin.readline()
    num = list(map(int, sys.stdin.readline().split()))
    sort_num = sorted(list(set(num)))
    dict_num = { sort_num[i]:i for i in range(len(sort_num)) }
    for i in num:
        print(dict_num[i], end=" ")

def main():
    # myCode()
    bestCode()
if __name__ == '__main__':
    main()