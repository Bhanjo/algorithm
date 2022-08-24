from itertools import permutations

def isPrime(permuList):
  cnt = 0
  check = []
  for i in permuList:
    isTrue = True
    for j in range(2, int(i)):
      if int(i) % j == 0:
        isTrue = False
        break
    if isTrue and int(i) >= 2 and int(i) not in check:
      cnt += 1
      check.append(int(i))
  return cnt

def solution(numbers):
    arr = [num for num in numbers]
    permu = []

    for i in range(1, len(numbers) + 1):
      permu += list(permutations(arr, i))
    
    permuList = [''.join(n) for n in permu]
    return isPrime(permuList)

# 2회차 (permutation 직접 구현 1회차 비교 6369ms -> 22ms 단축)
answer = 0
def solution(numbers):
    global answer
    numbers = list(numbers)
    visit = [False for _ in range(len(numbers))]
    check = {}
    temp = []
    
    def isPrime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        for i in range(2, int(n**(1/2))+1):
            if n % i == 0:
                return False
        return True
    
    def dfs():
        global answer
        num = ''.join(temp)
        if num != '':
            num = int(num)
        if num != '' and num not in check:
            check[num] = True
            if isPrime(num):
                answer += 1
        for i in range(len(numbers)):
            if not visit[i]:
                visit[i] = True
                temp.append(numbers[i])
                dfs()
                temp.pop()
                visit[i] = False
    
    dfs()
    return answer

print(solution("011"))