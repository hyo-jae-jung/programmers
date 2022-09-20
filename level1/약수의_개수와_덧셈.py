left, right = map(int,input().split())

def solution(left,right):
    numbers = range(left,right+1)
    aliquot_number_counts = [len([j for j in i if i[-1]%j == 0]) for i in [list(range(1,i+1)) for i in numbers]]

    return sum([i if j%2==0 else i*-1 for i,j in zip(numbers,aliquot_number_counts)])


if __name__ == "__main__":
    # print(solution(left,right))
    print(solution(left,right))
