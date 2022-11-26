from collections import deque
import pdb

X = '123213000087099664'
Y = '42509889031'




"""def solution(X,Y):
    
    answer = deque()
    X_d = deque(X)
    Y_d = deque(Y)
    
    while X_d and Y_d:
        # pdb.set_trace()
        x = X_d.popleft()
        if x in Y_d:
            if x == '0' and '0' in answer:
                continue
            else:
                answer.append(x)
            Y_d.remove(x)
    else:
        if len(answer) != 0:
            return ''.join(sorted(answer,reverse=True))
        else:
            return "-1"
    
    
    return answer """

"""def solution(X, Y):
    answer = ''

    if bool(set(X) & set(Y))==False:
        return "-1"
    else:
        for i in sorted(set(X),reverse=True):
            if i != '0':
                answer+=str(i)*Y.count(i)
            else:
                answer+=str(i)
        return answer
    """



if __name__ == "__main__":
    print(solution(X,Y))
