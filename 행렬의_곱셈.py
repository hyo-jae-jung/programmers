import numpy as np

def solution1(arr1, arr2):    
    return np.array(arr1) @ np.array(arr2)

def solution(arr1, arr2):
    answer = [[]]
    return answer

if __name__ == "__main__":
    arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
    arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
    print(solution1(arr1,arr2))
