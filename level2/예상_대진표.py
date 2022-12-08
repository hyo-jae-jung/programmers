import math
def solution(n:int,a:int,b:int)->int:
    max_cnt = int(math.log2(n))
    d = {j:i for i,j in enumerate(reversed(range(1,max_cnt+1)),1)}
    m=1
    while n>2**m:
        if (a-1)//(n/2**m) != (b-1)//(n/2**m):
            break
        m+=1

    return d[m]

if __name__ == "__main__":
    print(solution(8,4,7))
