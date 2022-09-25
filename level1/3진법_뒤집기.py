N = int(input())

def solution(n):

    def position_number(n:int) -> int:
        m = 1
        while n >= 3**m:m+=1
        return m-1

    n3_list = []
    m = position_number(n)
    while m >= 0:
        n3 = 0
        while n >= 3**m:
            n-=3**m
            n3+=1
        n3_list.append(n3)
        m-=1

    print(n3_list)
    return sum([(3**i)*j for i,j in enumerate(n3_list)])

if __name__ == "__main__":
    print(solution(N))
    