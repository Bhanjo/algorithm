def solution(N, number):
    patternSet = [0, [N]]
    if N == number:
        return 1
    
    # 최소값이 8 초과 => -1이므로 NNNNNNNNN = -1리턴됨 => 계산필요 x
    for i in range(2,9):
        allCase = []
        checkNumber = int(str(N) * i) # NN, NNN...
        allCase.append(checkNumber)
        for j in range(1, i//2+1):
            # 숫자가 i개일 때 i-1개일 때와 i-2개일 때의 숫자에 사칙연산을 추가 실행
            # i = 3일 때 5로 만들 수 있는 수
            # i-2개일 때 => (5+5)+5, (5+5)-5, (5+5)*5, (5+5)/5
            # i-1개일 때 => (55)+5, (55)-5, (55)/5, (55)*5
            for op1 in patternSet[j]:
                for op2 in patternSet[i-j]:
                    allCase.append(op1 + op2)
                    allCase.append(op1 - op2)
                    allCase.append(op2 - op1)
                    allCase.append(op1 * op2)
                    if op2 != 0:
                        allCase.append(op1/op2)
                    if op1 != 0:
                        allCase.append(op2/op1)
            if number in allCase:
                return i
            patternSet.append(allCase)
    return -1
    