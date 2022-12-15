import pdb

def solution(citations):
    citations.sort(reverse=True)
    print(citations)
    for i in citations:
        h = len([j for j in citations if j >= i]) 
        print(h)
        if h >= i:
            return i
    

if __name__ == "__main__":
    print(solution([3,0,6,1,5,5,4,1,0,0,4]))
