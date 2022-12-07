
"""효율성 0점

def solution(people:list,limit:int)->int:
    answer = 0
    while people:
        maximum_extra_value = limit-people.pop()
        correct_extra = [i for i in people if maximum_extra_value>=i]
        if correct_extra:
            people.remove(max(correct_extra))
        answer+=1
    return answer
"""

"""def solution(people:list,limit:int)->int:
    answer = len(people)
    people = [i for i in people if limit-min(people)>=i]
    answer -= len(people)
    while people:
        maximum_extra_value = limit-people.pop()
        correct_extra = [i for i in people if maximum_extra_value>=i]
        if correct_extra:
            people.remove(max(correct_extra))
        answer+=1

    return answer"""

"""효율성:0
def solution(people:list, limit:int)->int:
    cnt=0
    while people:
        one = people.pop()
        two = [i for i in people if limit-one>=i]
        if two:
            people.pop(people.index(max(two)))
        cnt+=1
    return cnt"""
people = [10,20,30,40,70,80]
limit = 80

import pdb
from collections import deque
def solution(people,limit):
    people = deque(sorted(people))
    a = 0
    z = 0
    cnt=0
    while people:
        z = people.pop()

        if not a and people:
            a = people.popleft()
        
        if a+z <= limit:
            a = 0
        z = 0
        cnt+=1
        
    else:
        if a:
            cnt+=1
    return cnt

if __name__ == "__main__":
    print(solution(people,limit))
