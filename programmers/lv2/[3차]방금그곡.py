import math


def solution(m, musicinfos):
    answer = '(None)'
    m = m.replace('A#', 'a').replace('C#', 'c'). replace('D#', 'd').replace('F#', 'f').replace('G#', 'g')

    check = []
    for music in musicinfos:
        start, end, title, melody = music.split(',')
        start = int(start[0:2]) * 60 + int(start[3:5])
        end = int(end[0:2]) * 60 + int(end[3:5])

        melody = melody.replace('A#', 'a').replace('C#', 'c'). replace('D#', 'd').replace('F#', 'f').replace('G#', 'g')
        melody *= math.ceil((end - start) / len(melody))
        melody = melody[:(end-start)]

        if m not in melody:
            continue
        else:
            check.append((start, (end-start), title))
    
    if len(check) > 0:
        check.sort(key=lambda x : x[1], reverse=True)
        answer = check[0][2]

    print(answer)
    return answer

# solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])
# solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])
# solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])
# solution("ABC#", ["12:12,12:21,WORLD,ABCABC#", "12:00,12:08,HELLO,ABC"])
solution("ABC", ["12:00,12:09,HELLO,ABC", "12:12,12:24,WORLD,ABC"])
# solution("CC#BCC#BCC#", ["03:00,03:08,FOO,CC#B"])