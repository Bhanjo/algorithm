def solution(n):
  bitN = bin(n)
  answer = n + 1
  while True:
    if bitN.count('1') == bin(answer).count('1'):
      return answer
    answer += 1
solution(67)