def solution(id_list, report, k):
    reportID = {name: [] for name in id_list}
    reportedID = {name: 0 for name in id_list}
    getEmail = {name: 0 for name in id_list}

    for i in report:
        name, target = map(str, i.split(" "))
        if target not in reportID[name]: # 중복 신고 방지
            reportID[name] += [target]
            reportedID[target] += 1

    for i in reportedID:
        if reportedID[i] >= k:
            for j in reportID:
                if i == j: continue
                if i in reportID[j]:
                    getEmail[j] += 1

    answer = [getEmail[i] for i in getEmail]
    return answer

solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
