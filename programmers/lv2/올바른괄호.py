def solution(s):
  st = []
  for i in s:
    if i == '(':
      st.append('(')
    else:
      if len(st) == 0:
        return False
      st.pop()
  if(len(st)):
    return False

  return True