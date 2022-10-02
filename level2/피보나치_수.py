n = int(input())

def solution(n):
    fibonacci_list = [0,1]
    for i in range(2,n+1):
        fibonacci_list.append(fibonacci_list[i-2]+fibonacci_list[i-1])
    return fibonacci_list[-1]%1234567

if __name__ == "__main__":
    print(solution(n))
