
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

def solution(id_list, report, k):
    report_intersection = iter(set(report))

    reporting = dict()
    reported = dict()
    for i in id_list:
        reporting[i]=[]
        reported[i]=0

    for i in report_intersection:
        temp = i.split()
        reporting[temp[0]].append(temp[1])
        reported[temp[1]]+=1

    temp = [i for i,j in reported.items() if j >= k]

    answer = []

    for i in id_list:
        answer.append(len(set(reporting[i])&set(temp)))

    return answer


if __name__ == "__main__":
    print(solution(id_list,report,k))
