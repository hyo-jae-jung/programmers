N = input()

def solution(x):
    zero_count = 0
    cycle = 0
    while True:
        cycle+=1
        zero_count+=x.count('0')
        n = x.count('1')
        if n==1:break
        temp = ''
        while n:
            temp+=str(n%2)
            n = n//2
        x = ''.join(reversed(temp))
    return [cycle,zero_count]

if __name__ == "__main__":
    print(solution(N))