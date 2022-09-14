N = int(input())
def solution(n):
    return sum(map(int,str(n)))

if __name__ == '__main__':
    print(solution(N))