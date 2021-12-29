def solution(answers):
    answer = []
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    answer_count = [0,0,0]
    for i,a in zip(range(len(answers)),answers):
        if s1[i%len(s1)] == a:
            answer_count[0] += 1
        if s2[i%len(s2)] == a:
            answer_count[1] += 1
        if s3[i%len(s3)] == a:
            answer_count[2] += 1
    for i,a in zip(range(1,4),answer_count):
        if a == max(answer_count):
            answer.append(i)

    return answer

print(solution(	[1, 3, 2, 4, 2]))