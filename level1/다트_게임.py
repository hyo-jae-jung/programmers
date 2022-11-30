import pdb

dartResult = '1T2D3D#'

def solution(dartResult):
    answer = ''
    temp = ''
    ans_list = []
    for i in dartResult:
        try:
            int(i)
            if answer:
                ans_list.append(answer)
                answer=''
            temp+=i
        except:
            if temp != '':
                answer+=temp
                temp=''
            if i == 'S':
                answer+='**1'
            elif i == 'D':
                answer+='**2'
            elif i == 'T':
                answer+='**3'
            elif i == '#':
                answer+='*(-1)'
            elif i == '*':
                answer+='*2'
                if ans_list:
                    ans_list[-1]+='*2'
    else:
        ans_list.append(answer)

    return eval('+'.join(ans_list))

print(solution(dartResult))
