left, right = map(int,input().split())

def solution(left,right):
    numbers = range(left,right+1)
    all_numbers = [list(range(1,i+1)) for i in numbers]
    aliquit_numbers = [j for i in all_numbers for j in i if i[-1]%j == 0]
    # aliquot_counts = [i for i in all_numbers if ]

    return aliquit_numbers

if __name__ == "__main__":
    # print(solution(left,right))
    print(solution(left,right))
