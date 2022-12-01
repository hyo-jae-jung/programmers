from itertools import combinations as comb
import pdb

s = 'ttomaato'

def solution(s):
    answer = []
    k = 2

    while len(s)>=2:
        temp = []
        # pdb.set_trace()
        for i in set(s[:k]):
            temp.append(s[:k].count(i))

        for i,j in comb(temp,2):
            if i==j:
                answer.append(s[:k])
                s = s[k:]
                k=2
                break
        else:
            k+=1
    else:
        answer.append(s)
        
    return answer

print(solution(s))
