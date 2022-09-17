N = input()

# def solution(s):
#     s = s.lower()
#     p_count = 0
#     y_count = 0
#     for i in s:
#         if i == 'p':
#             p_count+=1
#         elif i == 'y':
#             y_count+=1
#     if p_count+y_count != 0:
#         if p_count == y_count:
#             return True
#         else:
#             return False
#     else:
#         return True

def solution(s):
    return s.lower().count('p') == s.lower().count('y')


if __name__ == "__main__":
    print(solution(N))