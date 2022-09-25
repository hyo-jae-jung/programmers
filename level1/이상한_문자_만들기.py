N = input()

def solution(s):
    word_list = s.split(' ')
    new_word_list = []
    for i in word_list:
        new_word_list.append(''.join([k.upper() if j%2==0 else k.lower() for j,k in enumerate(i)]))
    return ' '.join(new_word_list)

if __name__ == "__main__":
    print(solution(N))
    
