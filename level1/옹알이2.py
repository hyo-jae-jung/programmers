import re

def solution(babbling):
    pronun = ["aya", "ye", "woo", "ma"]
    p = re.compile('\D*')
    temp = []
    for k in babbling:
        for i,j in enumerate(pronun,1):
            c = re.compile(j)
            k = c.sub(str(i),k)
        temp.append(k)
        
    temp2 = [i for i in temp if not any(p.findall(i))]
    temp3 = []
    for i in temp2:
        for j in ['11','22','33','44']:
            if j in i:
                break
        else:
            temp3.append(i)

    return len(temp3)

if __name__ == "__main__":

    babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
    print(solution(babbling))
