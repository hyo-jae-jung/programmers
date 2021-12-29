def solution(nums):
    answer = 0
    sum_numbers_list = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                temp = nums[i]+nums[j]+nums[k]
                # if temp not in sum_numbers_list:
                sum_numbers_list.append(temp)

    max_sum_numbers = max(sum_numbers_list)

    T_or_F = [False]*2 + [True]*(max_sum_numbers-1)
    for h in range(2,int((max_sum_numbers**0.5))+1):
        for i in range(h,len(T_or_F),h):
            if i != h and T_or_F[i]:
                T_or_F[i] = False

    print(sum_numbers_list)
    print(T_or_F)

    for i in sum_numbers_list:
        if T_or_F[i]:
            answer += 1

    return answer

print(solution([1,2,3,4,5,6]))