d = list(map(int,input().split()))
budget = int(input())

def solution(d, budget):
    d.sort()
    for i in range(len(d)):
        if budget < sum(d[:i+1]): return len(d[:i])
        elif budget == sum(d[:i+1]): return len(d[:i+1])
    return len(d)        

if __name__ == "__main__":
    print(solution(d,budget))
