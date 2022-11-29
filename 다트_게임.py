import pdb

dartResult = '1D2S#10S'

answer = 0
temp = ''
for i in dartResult:
    # pdb.set_trace()
    try:
        int(i)
        temp+=i
    except:
        temp2=int(temp)
        temp = ''
        if i == 'S':
            temp2**=1
        elif i == 'D':
            temp2**=2
        elif i == 'T':
            temp2**=3
        elif i == '#':
            temp2*=-1
        elif i == '*':
            answer*=2
            temp2*=2
else:
    if temp>0:
        answer+=temp

print(answer)
