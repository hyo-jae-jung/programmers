from collections import deque

def solution(s):
    s = deque(reversed(s))
    answer = deque()
    while s:
        temp = s.popleft()
        if temp in s:
            answer.appendleft(s.index(temp)+1)
        else:
            answer.appendleft(-1)
    return list(answer)

if __name__ == "__main__":
    print(solution('foobar'))
