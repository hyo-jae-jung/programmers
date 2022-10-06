# N = int(input())
# stages = map(int,input().split())
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

def solution(N,stages):
    answer = []
    users_num = len(stages)
    for i in range(1,N+1):
        answer.append((i,stages.count(i)/users_num if users_num else 0))
        users_num-=stages.count(i)
    return [i[0] for i in sorted(answer,key=lambda x:x[1],reverse=True)]
if __name__ == "__main__":
    print(solution(N,stages))
