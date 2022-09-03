num = int(input())

for i in range(0,num) :
    for j in range(0,num) :
        if(j >= num-i-1) :
            print("*", end='')
        else :
            print("", end=" ")
    print()