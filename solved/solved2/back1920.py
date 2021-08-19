import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int,input().split()))

def find_num(num, start, end):
    if start > end:
        return print(0)
    middle_point = (start+end)//2
    # print("스타트: ", start, "엔드: ", end, "미들", middle_point)
    if num == n_list[middle_point]:
        return print(1)
    elif num < n_list[middle_point]:
        return find_num(num, start, middle_point-1)
    else:
        return find_num(num, middle_point+1, end)

for i in m_list:
    find_num(i, 0, len(n_list)-1)