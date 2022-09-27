n = int(input())

def solution(n):
    a = 1
    while bin(n)[2:].count('1') != bin(n+a)[2:].count('1'):a+=1
    return n+a

if __name__ == "__main__":
    print(solution(n))
