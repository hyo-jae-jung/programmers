from itertools import combinations
import numpy as np

d = list(map(int,input().split()))
budget = int(input())

def solution(d, budget):   
    department_count = len(d)
    while department_count > 0:
        if (True and 0) in list(budget - np.array(list(map(sum,combinations(d,department_count))))):
            return department_count
        department_count-=1

if __name__ == "__main__":
    print(solution(d,budget))
