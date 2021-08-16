# 에리토스테네스의 체
import time

def is_prime(num):
    n = 2
    while(True) :
        a = [False,False] + [True]*(n-1)
        prime=[]
        cnt = 0

        for i in range(2, n+1) : 
            if a[i]:
                prime.append(i)
                cnt += 1
                for j in range(2*i, n+1, i) :
                    a[j] = False

        if cnt >= num :
            return print(prime)
            break
        
        n+=1

num = int(input('Length? '))

start = time.time()
is_prime(num)