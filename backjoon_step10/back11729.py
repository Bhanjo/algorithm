def hanoi(num,a,b,c):
    if(num == 1):
        print(a, c)
    else:
        hanoi(num-1,a,c,b)
        print(a,c)
        hanoi(num-1,b,a,c)

num = int(input())
print((2**num)-1)
hanoi(num,1,2,3)