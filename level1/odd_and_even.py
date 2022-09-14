N = int(input())

def solution(num):

    answer = ''
    if num%2 == 0:
        answer = 'Even'
    else:
        answer = 'Odd'
    return answer

if __name__ == "__main__":
    print(solution(N))
