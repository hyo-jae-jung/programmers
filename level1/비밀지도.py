n = int(input())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

def solution(n,arr1,arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        temp = ""
        for k,l in zip(bin(i)[2:].zfill(n),bin(j)[2:].zfill(n)):
            if (k == '1' or l == '1'):
                temp+='#'
            elif k == '0' and l == '0':
                temp+=' '
        answer.append(temp)
    return answer

if __name__ == "__main__":
    print(solution(n,arr1,arr2))
