def solution(s):
  nums = list(map(int, s.split()))
  values = [str(min(nums)), str(max(nums))]
  answer = ' '.join(values)
  return answer
solution("-1 -2 -3 -4")