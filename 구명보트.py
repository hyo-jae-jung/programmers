people = list(map(int,input().split()))
limit = int(input())

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

def solution(people:list,limit:int)->int:
    answer = len(people)
    people = [i for i in people if limit-min(people)>=i]
    answer -= len(people)
    while people:
        maximum_extra_value = limit-people.pop()
        correct_extra = [i for i in people if maximum_extra_value>=i]
        if correct_extra:
            people.remove(max(correct_extra))
        answer+=1

    return answer

if __name__ == "__main__":
    print(solution(people,limit))