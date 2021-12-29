def solution(n, lost, reserve):
    real_lost = list(set(lost)-set(reserve))
    real_reserve = list(set(reserve)-set(lost))
    answer = n - len(real_lost)

    for i in real_lost:
        if i-1 in real_reserve:
            real_reserve.remove(i-1)
            answer += 1
        elif i+1 in real_reserve:
            real_reserve.remove(i+1)
            answer += 1

    return answer

print(solution(5,[2,4],[1,3,5]))
print(solution(5,[2,4],[3]))
print(solution(3,[3],[1]))