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

print(solution("011"))