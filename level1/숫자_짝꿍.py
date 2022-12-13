X = '100'
Y = '200'

def solution(X,Y):
    d = dict()
    X = sorted(X,reverse=True)
    Y = sorted(Y,reverse=True)
    
    for i in reversed(range(10)):
        i=str(i)
        x_cnt = X.count(i)
        X = X[x_cnt:]
        y_cnt = Y.count(i)
        Y = Y[y_cnt:]
        d[i]=min(x_cnt,y_cnt)
    answer = ''
    temp_list = list(d.values())
    
    if sum(temp_list) == 0:
            answer = '-1'    
    elif sum(temp_list[:-1]) > 0:
        answer = ''.join([i*j for i,j in d.items()])
    elif sum(temp_list[:-1]) == 0 and temp_list[-1] > 0:
        answer = '0'

    return answer


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
