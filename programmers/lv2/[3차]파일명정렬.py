def solution(files):
    sortToFiles = {}
    nums = ''
    strs = ''
    for i in files:
        sortToFiles[i] = []
        for word in i:
            if len(nums) > 0 and not '0' <= word <= '9':
                break
            if '0' <= word <= '9':
                nums += word
            else:
                strs += word
        sortToFiles[i].append(strs.upper())
        sortToFiles[i].append(int(nums))
        nums = ''
        strs = ''
    
    answer = list(sortToFiles.items())
    answer.sort(key = lambda x: (x[1][0], x[1][1]))
    ans = []
    for i in answer:
        ans.append(i[0])
    return ans

# 정규식을 이용한 풀이
import re
def solution(files):
    temp = [re.split(r"([0-9]+)", s) for s in files]
    print(temp)
    sort = sorted(temp, key = lambda x: (x[0].lower(), int(x[1])))
    
    return [''.join(s) for s in sort]
solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])

# 2회차
def solution(files):
    answer = []
    temp = []
    
    for file in files:
        # originHead, head, number, originNumber, tail
        div = ['','','','','']
        numCnt = 0
        
        for i, word in enumerate(file):
            if not word.isdigit() and len(div[2]) == 0: # head 판별
                div[0] += word
                div[1] += word
            elif word.isdigit(): # number 판별
                if numCnt < 5:
                    div[2] += word
                    div[3] += word
                    numCnt += 1
                if numCnt >= 5: # 나머지 tail
                    div[4] += file[i+1:]
                    break
            else: # 나머지 tail
                div[4] += file[i:]
                break
        
        # 소문자, 숫자 변환
        div[1] = div[1].lower()
        div[2] = int(div[2])
        temp.append(div)
    
    temp.sort(key=lambda x:(x[1],x[2]))
    for i in temp:
        answer.append(i[0] + i[3] + i[4])
    
    return answer