def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        if int(t[0+i:len(p)+i]) <= int(p):
            answer+=1
    return answer

if __name__ == "__main__":
    t = '3141592'
    p = '271'
    print(solution(t,p))
