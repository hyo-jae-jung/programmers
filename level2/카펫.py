brown = int(input())
yellow = int(input())

def solution(brown,yellow):
    aliquot = [i for i in range(1,brown+yellow+1) if (brown+yellow)%i == 0]
    return sorted([[[i,j] for j in aliquot if i+j == brown/2+2 and i*j == brown+yellow] for i in aliquot],reverse=True)[0][0]

if __name__ == "__main__":
    print(solution(brown,yellow))
