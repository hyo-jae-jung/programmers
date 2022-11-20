""" false : time over
def aliquot_list(n):
    return len([i for i in range(1,n+1) if n%i==0])

def solution(number, limit, power):
    answer = []
    for i in range(1,number+1):
        temp = aliquot_list(i)
        if temp <= limit:
            answer.append(temp)
        else:
            answer.append(power)
    return sum(answer)   
"""
if __name__ == "__main__":
    print(solution(10,3,2))
