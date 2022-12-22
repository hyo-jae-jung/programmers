import re

rs = re.compile('\(\)')
rm = re.compile('\{\}')
rl = re.compile('\[\]')

def solution(s):
    answer = 0
    cnt=0
    s_temp = s
    for _ in range(len(s)-1):
        while s_temp and cnt < 6:

            s_temp = rs.sub('',s_temp)
            print(s_temp)
            s_temp = rm.sub('',s_temp)
            print(s_temp)
            s_temp = rl.sub('',s_temp)
            print(s_temp)
            cnt+=1
        else:
            if s_temp == '':
                answer+=1
        s_temp = s
        
    return answer

if __name__ == "__main__":
    s = "[](){}"
    print(solution(s))

