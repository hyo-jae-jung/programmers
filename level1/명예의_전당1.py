def solution(k, score):
    answer = []
    temp = []
    for i in score:
        temp.append(i)
        temp.sort(reverse=True)
        temp = temp[:k]
        answer.append(min(temp))
    return answer


if __name__ == "__main__":
    print(solution(4,[0,300,40,300,20,70,150,50,500,1000]))
