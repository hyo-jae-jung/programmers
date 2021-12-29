def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append('dummy')
    for p,c in zip(participant,completion):
        if p != c:
            return p

print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))    
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))

# https://docs.python.org/ko/3/library/collections.html 다른사람 풀이에서 해당 패키지의 counter 메소드로 푼 풀이가 간결함. 공부해보기
# set 메소드도 잘 쓰면 좋은데 중복을 허용하지 않아서 불가