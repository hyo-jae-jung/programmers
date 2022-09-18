N = int(input())

def solution(num):
    count = 0
    
    while num != 1:
        if num%2 == 0:
            num/=2
        else:
            num = num*3+1
        count+=1
        if count == 500:
            break
    
    if count < 500:
        return count
    else:
        return -1

if __name__ == "__main__":
    print(solution(N))
