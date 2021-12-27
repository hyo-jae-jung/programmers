import math

# def solution(dicimal_number:int):
#     temp = ''
#     from_dicimal_system_to_country124_system = {
#         1:'1',
#         2:'2',
#         0:'4',
#                  }
#     digit_number = 1
#     sum_position_numbers = 0
#     while True:
#         sum_position_numbers += 3**(digit_number-1)
#         digit_number += 1
#         if math.ceil(dicimal_number/3) < sum_position_numbers + 3**(digit_number-1):
#             break

#     print(digit_number)

#     temp += str(from_dicimal_system_to_country124_system[dicimal_number%3])
#     dicimal_number = math.ceil(dicimal_number/3) - sum_position_numbers
    
#     while True:
#         if dicimal_number >= 3:
#             temp += from_dicimal_system_to_country124_system[dicimal_number%3]
#             dicimal_number = math.ceil(dicimal_number/3)
#         if dicimal_number < 3:
#             temp += from_dicimal_system_to_country124_system[dicimal_number]
#             break

#     while len(temp) < digit_number:
#         temp += '1'
#     answer = ''
#     for i in reversed(list(temp)):
#         answer += i

#     return answer

def solution(dicimal_number:int):
    digit_number = 1
    sum_digit_numbers = 0
    while dicimal_number > sum([3**i for i in range(0,digit_number)]):
        sum_digit_numbers += 3**digit_number
        digit_number += 1
    print(digit_number,sum_digit_numbers)
    


solution(1)
solution(2)
solution(3)
solution(4)
solution(5)
solution(6)
solution(7)
solution(8)
solution(9)
solution(10)
solution(11)
solution(12)
solution(13)
