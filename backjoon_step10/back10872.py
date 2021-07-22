def facto(num):
    if(num == 1 or num == 0):
        return 1
    else:
        return num * facto(num-1)

num = int(input())
print(facto(num))