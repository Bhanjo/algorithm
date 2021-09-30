a = int(input())
num = a
new_num = 0
tmp = 0
cnt = 0

# 핵심은 두 자리 수를 어떻게 분리할 것인가
while(True) :
    cnt += 1
    tmp = a//10 + a%10 #몫과 나머지로 수를 분리
    new_a = (a%10)*10 + tmp%10
    a = new_a
    if(new_a == num) :
        print(cnt)
        break