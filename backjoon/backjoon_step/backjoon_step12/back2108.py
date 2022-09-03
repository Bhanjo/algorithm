import sys
from typing import Counter

def myCode():
    a = int(sys.stdin.readline())
    num = []*a

    for _ in range(a):
        num.append(int(sys.stdin.readline()))
    
    sort_num = sorted(num)
    
    num_cnt = Counter(sort_num).most_common()

    print(round(sum(num)/a))
    print(sort_num[(a//2)])
    
    if(len(num_cnt)) > 1:
        if num_cnt[0][1] == num_cnt[1][1]:
            print(num_cnt[1][0])
        else:
            print(num_cnt[0][0])
    else:
        print(num_cnt[0][0])

    print(max(num)-min(num))

def main():
    myCode()
if __name__ == '__main__':
    main()