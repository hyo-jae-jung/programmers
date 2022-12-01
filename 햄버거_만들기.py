""" 정규표현식으로는 안됨. 순서가 달라서 꼬임
import re
def solution(ingredient):
    result = 0
    temp = ''.join(map(str,ingredient))
    temp2 = ''
    p = re.compile('1231')
    while True:
        m = p.sub('.',temp)
        result += m.count('.')
        temp = ''.join(m.split('.'))
        if temp == temp2:
            break
        temp2 = temp
    return result"""

import pdb

def solution(ingredient):
    cnt = 0
    hamburger = [1,2,3,1]
    while True:
        for i in range(4,len(ingredient)+1):
            if ingredient[i-len(hamburger):i] == hamburger:
                del ingredient[i-len(hamburger):i]
                cnt+=1
                break
        else:
            return cnt



if __name__ == "__main__":
    print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))
    