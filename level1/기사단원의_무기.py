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
def solution(number,limit,power):

    def aliquot_list(n):
        temp = 0
        for i in range(1,int(n**(1/2))+1):
            if n%i==0:
                temp+=1
                if i != n//i:
                    temp+=1

            if temp > limit: 
                return power

        return temp

    return sum(aliquot_list(i) for i in range(1,number+1))

if __name__ == "__main__":
    print(solution(10,3,2))
