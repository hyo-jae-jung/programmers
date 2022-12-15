def solution(citations):
    citations.sort(reverse=True)
    i=max(citations)
    while True:
        h = len([j for j in citations if j >= i])
        if h >= i:
            break
        i-=1
    return i
    

if __name__ == "__main__":
    print(solution([3,0,6,1,5,5,4,1,0,0,4]))
