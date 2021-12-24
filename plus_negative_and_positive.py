def solution(absolutes, signs):
    answer = 0
    for s,a in zip(signs,absolutes):
        if s:
            answer += a
        else:
            answer -= a
    return answer

