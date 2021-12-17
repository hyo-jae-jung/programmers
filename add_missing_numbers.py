def solution(numbers):
    a = set(range(0,10))
    b = set(numbers)
    answer = sum(a-b)
    return answer