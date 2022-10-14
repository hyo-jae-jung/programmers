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

# # 실패1

# from collections import deque

# def solution(s):
#     deq = deque(s)
#     if len(deq)%2==0 and 1 not in [deq.count(i)%2 for i in set(deq)]:
#         cnt = 0
#         while deq:
#             print(deq)
#             if deq[-1] == deq[-2]:
#                 deq.pop()
#                 deq.pop()
#                 cnt = 0
#             else:
#                 deq.rotate(1)
#                 cnt+=1
#                 if cnt == len(deq):
#                     return 0
#         return 1
#     else:
#         return 0
# 실패2

def solution(s):
    s_list = list(s)
    if len(s_list)%2==0 and 1 not in [s_list.count(i)%2 for i in set(s_list)]:
        while True:
            temp = []
            while s_list:
                print(s_list,temp)
                if s_list[-1]==s_list[-2]:
                    s_list.pop()
                    s_list.pop()
                else:
                    temp.append(s_list.pop())

            s_list = temp
        return
    else:
        return 0

if __name__ == "__main__":
    print(solution(s))
