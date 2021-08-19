import sys
input = sys.stdin.readline

while(True):
    n = int(input())
    if n == 0:
        break;
    num_list = list(map(int,str(n)))
    reverse_list = num_list[::-1]
    check_num = False
    for i in range(len(num_list)//2 + 1):
        if num_list[i] != reverse_list[i]:
            check_num = False
            break
        else:
            check_num = True
    if check_num:
        print("yes")
    else:
        print("no")