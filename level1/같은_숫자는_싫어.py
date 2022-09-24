N = list(map(int,input().split()))

from collections import deque

def solution(arr):
    
    answer = deque()
    d = deque(arr)
    answer.append(d.popleft())

    for _ in range(len(d)):
        if answer[-1] == d[0]:
            d.popleft()
        else:
            answer.append(d.popleft())
    
    return list(answer)

if __name__ == "__main__":
    print(solution(N))
    