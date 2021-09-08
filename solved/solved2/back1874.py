tc = int(input())

stack = []
result = []
nums = [n+1 for n in range(tc)]
prt = []
for _ in range(tc):
    result.append(int(input()))

i = 0
cnt = 0
while(True):
    if len(stack) == 0:
        stack.append(nums[i])
        prt.append('+')
        i += 1
    else:
        if stack[len(stack)-1] == result[cnt]:
            stack.pop()
            prt.append('-')
            cnt += 1
        else:
            if i == tc:
                print('NO')
                break
            stack.append(nums[i])
            prt.append('+')
            i += 1

    if cnt == tc:
        for i in prt:
            print(i)
        break

# 최적 코드
# n = int(input())
# s = []
# op = []
# count = 1
# temp = True
# for i in range(n):
#     num = int(input())
#     while count <= num:
#         s.append(count)
#         op.append('+')
#         count += 1
#     if s[-1] == num:
#         s.pop()
#         op.append('-')
#     else:
#         temp = False
# if temp == False:
#     print('NO')
# else:
#     for i in op:
#         print(i)
