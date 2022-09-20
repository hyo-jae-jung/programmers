def solution(arr1, arr2):
    y = []
    for i,j in zip(arr1,arr2):
        x = []
        for k,l in zip(i,j):
            x.append(k+l)
        y.append(x)
    return y
