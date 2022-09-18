N = int(input())

def solution(n):
    for i in range(1,n):
        if n%i == 1:
            return i

if __name__ == "__main__":
    print(solution(N))
    