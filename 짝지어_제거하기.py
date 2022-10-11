s = input()

# def solution(s):

#     if len(s)%2==1:
#         return 0

#     for i in list(set(s)):
#         if s.count(i)%2 == 1:
#             return 0

#     origin = list(s)
#     s_list = origin
#     while origin:
#         for i in reversed(range(len(s_list)-1)):
#             if s_list[i] == s_list[i+1]:
#                 s_list.pop(i)
#                 s_list.pop(i)
#         if origin == s_list:
#             return 0
#         else:
#             origin = s_list

#     return 1

# 실패

if __name__ == "__main__":
    print(solution(s))
