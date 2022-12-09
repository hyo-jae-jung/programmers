def solution(s):
    s = s.lower()
    p_cnt=s.count('p')
    y_cnt=s.count('y')
    answer = True
    if p_cnt + y_cnt == 0:
        answer = True
    elif p_cnt == y_cnt:
        answer = True
    else:
        answer = False
    return answer