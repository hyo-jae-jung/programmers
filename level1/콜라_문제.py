a,b,n = map(int,input().split())
def solution(a,b,n):

    result = 0
    while n>=a:
        result+=(n//a)*b
        n = (n//a)*b+n%a

    return result
if __name__ == "__main__":
    print(solution(a,b,n))
