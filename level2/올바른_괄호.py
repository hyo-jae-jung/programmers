s = input()

def solution(s):
    if s.count('(') != s.count(')') or s[0] != '(' or s[-1] != ')':
        return False
    else:
        temp = 0
        for i in s:
            if i == '(':
                temp+=1
            elif i == ')':
                temp-=1
            
            if temp<0:return False

    return True if temp == 0 else False

if __name__ == "__main__":
    print(solution(s))
