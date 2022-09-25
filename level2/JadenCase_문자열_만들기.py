N = list(input().split(' '))

def solution(n):
    return ' '.join([i[:1].upper()+i[1:].lower() for i in n])

if __name__ == "__main__":
    print(solution(N))
