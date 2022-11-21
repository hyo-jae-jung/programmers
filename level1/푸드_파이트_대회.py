food = [1,3,4,6]

def solution(food):
    answer = ''
    for i in range(1,len(food)):
        answer+=str(i)*(food[i]//2)
    return answer + str(0) + ''.join(reversed(answer))

if __name__ == "__main__":
    print(solution(food))
