def solution(phone_book):
  phone_book.sort()
  for i in range(len(phone_book) - 1):
    # 정렬된 문자열 비교하기
    if len(phone_book[i]) < len(phone_book[i+1]):
      # 뒤에 문자열에서 0~len(앞자리문자열) 이 앞 자리 문자열과 같으면 접두사 일치
      if phone_book[i+1][:len(phone_book[i])] == phone_book[i]:
        return False
  return True

  # 정석풀이
  def solution(phone_book):
    answer = True
    hash_map = {}

    # dict로 번호를 key, 1을 value로 지정
    for phone_number in phone_book:
        hash_map[phone_number] = 1

    for phone_number in phone_book:
        temp = ""
        # 번호를 하나씩 추가하기
        for number in phone_number:
            temp += number
            # temp에 하나씩 추가된 번호가 해시맵에 있다면 접두사 일치
            # 단, 원본 번호와는 겹치면 안된다
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer