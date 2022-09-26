n = int(input())

def solution(n):
    count = 0
    S = n
    n = 1
    while True:
        a = S/n + 1/2 - n/2
        if a == int(a):count+=1
        n+=1
        if a <= 1:break
    return count

if __name__ == "__main__":
    print(solution(n))
