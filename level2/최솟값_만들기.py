A = list(map(int,input().split()))
B = list(map(int,input().split()))

def solution(A,B):
    return sum([i*j for i,j in zip(sorted(A),sorted(B,reverse=True))])

if __name__ == "__main__":
    print(solution(A,B))


