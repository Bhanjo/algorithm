def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        binary1 = []
        binary2 = []
        row = []
        
        # arr1의 이진수 구하기
        while(arr1[i]):
            binary1.append(arr1[i] % 2)
            arr1[i] = arr1[i] // 2
        
        if len(binary1) < n: # 길이 맞추기
            while(len(binary1) < n):
                binary1.append(0)
        binary1.reverse()
        
        # arr2의 이진수 구하기
        while(arr2[i]):
            binary2.append(arr2[i] % 2)
            arr2[i] = arr2[i] // 2
            
        if len(binary2) < n: # 길이 맞추기
            while(len(binary2) < n):
                binary2.append(0)
        binary2.reverse()
        
        # 지도 합치기
        for j in range(n):
            if binary1[j] == 1 or binary2[j] == 1:
                row.append('#')
            elif binary1[j] == 0 and binary2[j] == 0:
                row.append(' ')
                
        answer.append(''.join(row))
    return answer