def solution(num):
    cnt = 0
    while num != 1:
        if num%2 == 0:
            num/=2
        else:
            num = num*3+1
        cnt+=1
        if cnt == 500 and num != 1:
            return -1
    return cnt

if __name__ == "__main__":
    print(solution(626331))
