def solution(clothes):
  answer = 1
  arr = {}
  # 딕셔너리 만들기
  for i in clothes:
    if arr.get(i[1]):
      arr[i[1]].append(i[0])
    else:
      arr[i[1]] = [i[0]]
  
  # 조합 경우의 수 구하기
  num = []
  for i in arr:
    num.append(len(arr[i]))
  for i in num:
    answer *= (i+1)
  return answer - 1

# best
def solution(clothes):
  answer = {}
  for i in clothes:
    if i[1] in answer:
      answer[i[1]] += 1
    else:
      answer[i[1]] = 1
  cnt = 1
  for i in answer.values():
    cnt *= i+1
  return cnt - 1

solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])