number = map(int,input().split())

from itertools import combinations as cb

def solution(number):
    return list(map(sum,cb(number,3))).count(0)

if __name__ == "__main__":
    print(solution(number))