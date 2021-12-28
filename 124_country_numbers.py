def solution(n):
    temp = []
    while n/3 > 0:
        if n%3 == 0:
            temp.append(4)
            n = n//3 - 1
        else:
            temp.append(n%3)
            n = n//3
    return ''.join(str(i) for i in reversed(temp))


print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
print(solution(7))
print(solution(8))
print(solution(9))
print(solution(20))
print(solution(30))
print(solution(32))