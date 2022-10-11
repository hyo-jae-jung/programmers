s = input()

def solution(s):

    if len(s)%2==1:
        return 0

    for i in list(set(s)):
        if s.count(i)%2 == 1:
            return 0

    s_list = list(s)

    while s_list:
        start = s_list
        for i in range(len(s_list)-1):
            if s_list[i] == s_list[i+1]:
                s_list.pop(i)
                s_list.pop(i)
        if start == s_list:
            return 0
    return 1

if __name__ == "__main__":
    print(solution(s))
