n,m = map(int,input().split())

def solution(n, m):
    a = [i for i in range(1,n+1) if n%i == 0]
    b = [i for i in range(1,m+1) if m%i == 0]
    c = [n*i for i in range(1,m+1)]
    d = [m*i for i in range(1,n+1)]
    return [max(set(a) & set(b)),min(set(c)&set(d))]

if __name__ == "__main__":
    print(solution(n,m))
    