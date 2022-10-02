n = int(input())
# words = input().split()
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
words1 = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
words2 = ["hello", "one", "even", "never", "now", "world", "draw"]

def solution(n,words):
    temp_list = []
    temp_list.append(words.pop(0))
    for i in words:
        if i in temp_list or temp_list[-1:][0][-1:] != i[:1]:
            error_num = len(temp_list)+1
            return [error_num%n if error_num%n != 0 else n, error_num//n+(0 if error_num/n == error_num//n else 1)]
        else:
            temp_list.append(i)
    return [0,0]

if __name__ == "__main__":
    print(solution(n,words1))

