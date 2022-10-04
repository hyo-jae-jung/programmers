n = int(input())

def solution(n):
    return [[i for i in range(2,j+1) if j%i] for j in range(2,n+1)]

if __name__ == "__main__":
    print(solution(n))
