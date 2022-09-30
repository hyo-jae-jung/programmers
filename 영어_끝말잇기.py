n = int(input())
# words = input().split()
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
import math

def solution(n,words):
    temp_list = []
    temp_list.append(words.pop(0))
    print(words)
    for i in words:
        if i not in temp_list:
            temp_list.append(i)
            print(temp_list)
            print(temp_list[-2:-1][0][-1:])
            print(temp_list[-1:][0][:1])
            if temp_list[-2:-1][0][-1:] != temp_list[-1:][0][:1]:
                return [len(temp_list)%n, math.ceil(len(temp_list)/n)]
        else:
            return [(len(temp_list)+1)%n, math.ceil(len(temp_list)/n)]

    return [0,0]

if __name__ == "__main__":
    print(solution(n,words))

# commit....
