def myCode():
    tc = int(input())
    num = list(map(int, input().split()))
    cnt = 0
    for i in num:
        if(i < 2):
            continue
        else:
            nanum = 2
            while(True):
                if(i == nanum):
                    cnt += 1
                    break
                if(i % nanum == 0):
                    break
                nanum += 1
    print(cnt)

# 에라토스테네스의 체
# def isPrime(n):
# 	if n <= 1:
# 		return False
# 	i = 2
# 	while i*i <= n:
# 		if n%i == 0:
# 			return False
# 		i += 1
# 	return True
# input()
# ans = 0
# for n in map(int, input().split()):
# 	if isPrime(n):
# 		ans += 1
# print(ans)

def main():
    myCode()
if __name__ == '__main__':
    main()