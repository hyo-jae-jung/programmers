N = int(input())

def solution(x):
    return x%sum(map(int,list(str(x)))) == 0

if __name__ == "__main__":
    print(solution(N))
