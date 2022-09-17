N=int(input())

# def solution(n):
#     temp = list(map(str,sorted(list(map(int,list(str(n)))),reverse=True)))
#     answer = ''
#     for i in temp:
#         answer+=i
#     return int(answer)

def solution(n):
    return int(''.join(sorted(list(str(n)),reverse=True)))


if __name__ =="__main__":
    print(solution(N))