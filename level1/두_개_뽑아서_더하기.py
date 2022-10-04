numbers = map(int,input().split())

from itertools import combinations

def solution(numbers):
    return list(sorted(set(map(sum,combinations(numbers,2)))))

if __name__ == "__main__":
    print(solution(numbers))