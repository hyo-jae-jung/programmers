def factorial(n,m):
    return eval('*'.join(map(str,range(m+1,n+1)))) if n > 0 else 1

def solution(n):
    temp='1'*n
    answer = 1
    while temp.count('1') >=2:
        temp = temp[2:]
        temp+='2'
        answer+=factorial(len(temp),temp.count('1'))//factorial(temp.count('2'),0)
    return int(answer) % 1234567

if __name__ == "__main__":
    print(solution(2000))
