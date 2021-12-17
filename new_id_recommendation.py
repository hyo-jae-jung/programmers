import re

def solution(new_id):
    answer = new_id.lower() # step :1
    answer = re.sub('[^a-z0-9-_.]', '',answer) # step : 2
    answer = re.sub('[.]{2,}','.',answer) # step : 3
    answer = answer.strip('.') # step : 4
    if len(answer) == 0: # step : 5
        answer += 'a'
    answer = answer[0:15].strip('.') # step : 6
    while len(answer) < 3: # step : 7
        if len(answer) <= 2:
            answer += answer[-1]
    return answer

print(solution("abcdefghijklmn.p"))