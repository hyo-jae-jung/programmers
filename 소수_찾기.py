n = int(input())

# from itertools import takewhile

# def solution1(n):
#     return sum([True for i in range(2,n+1) if len([j for j in takewhile(lambda x:i%x!=0,range(2,i))])==i-2])


# def solution2(n):
#     def sosu(n):
#         for i in range(2,n):
#             if n%i==0:return False
#         else:return True
#     sosu_list = []
#     for i in range(2,n+1):
#         sosu_list.append(sosu(i))
#     return(sum(sosu_list))

# 에라토스테네스의 체로 풀어야 하는 문제

def solution(n):
    a = [False,False] + [True]*(n-1)
    primes=[]

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    return len(primes)

if __name__ == "__main__":
    print(solution(n))
