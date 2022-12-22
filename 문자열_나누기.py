from collections import deque

s = 'aaaaccc'

def solution(s):
    s_dict = {i:0 for i in s}
    s = deque(s)
    answer = deque()
    temp = ''
    while s:
        a = s.popleft()
        temp+=a
        s_dict[a]+=1
        v = [i for i in s_dict.values() if i > 0]
        if len(set(v)) != len(v):
            answer.append(temp)
            temp = ''
            s_dict = {i:0 for i in s}
    else:
        answer.append(temp)

    return [i for i in answer if i]

print(solution(s))
