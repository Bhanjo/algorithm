def solution(citations):
  citations.sort()
  hIndex = 0
  for i in range(1, citations[len(citations) - 1]):
    cnt = 0
    for j in citations:
      if j >= i:
        cnt += 1
    if cnt >= i:
      hIndex = i
    else:
      break
  return hIndex