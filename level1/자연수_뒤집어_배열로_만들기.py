N=int(input())

def solution(n):    
    return list(map(int,str(n)))[::-1]

if __name__ == "__main__":
    print(solution(N))