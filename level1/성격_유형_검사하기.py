import pdb

survey = ["TR", "RT", "TR"]
choices = [7, 1, 3]

def solution(survey, choices):
    char_list = ['RT','CF','JM','AN']
    temp = {i:0 for i in char_list}

    for i,j in zip(survey,choices):
        if i in char_list:
            temp[i]+=j-4
        else:
            temp[''.join(reversed(list(i)))]+=-1*(j-4)

    answer = ''

    for i in char_list:
        if temp[i]<=0:
            answer+=i[0]
        else:
            answer+=i[1]

    return answer

if __name__ == "__main__":
    print(solution(survey, choices))
