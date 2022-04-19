def solution(w,h):
    answer = w * h
    def gcd(w,h):
        minVal, maxVal = min(w,h), max(w,h)
        while(True):
            result = maxVal%minVal
            if result == 0:
                return minVal
            maxVal = minVal
            minVal = result
    return answer - (w+h-gcd(w,h))
    
solution(8,12)