N=input()
def solution(s):
    int_list = list(map(int,s.split()))
    int_list.sort()
    return str(int_list[0])+' '+str(int_list[-1])

if __name__ == "__main__":
    print(solution(N))
    